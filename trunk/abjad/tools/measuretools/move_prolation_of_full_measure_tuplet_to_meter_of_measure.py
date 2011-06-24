from abjad.tools import mathtools
from abjad.tools.measuretools.iterate_measures_forward_in_expr import iterate_measures_forward_in_expr
from abjad.tools import durtools


def move_prolation_of_full_measure_tuplet_to_meter_of_measure(expr):
   r'''Subsume all measures in expr containing only top-level tuplet.
   Measures usually become nonbinary as as result of subsumption.

   Return none.

   Example::

      abjad> t = Measure((2, 8), [tuplettools.FixedDurationTuplet(Duration(2, 8), "c'8 d'8 e'8")])
      abjad> measuretools.move_prolation_of_full_measure_tuplet_to_meter_of_measure(t)
      abjad> f(t)
      {
         \time 3/12
         \scaleDurations #'(2 . 3) {
            c'8
            d'8
            e'8
         }
      }

   .. versionchanged:: 1.1.2
      renamed ``measuretools.subsume( )`` to
      ``measuretools.move_prolation_of_full_measure_tuplet_to_meter_of_measure( )``.
   '''
   from abjad.tools.tuplettools.Tuplet import Tuplet
   from abjad.tools import componenttools
   from abjad.tools import contexttools
   from abjad.tools import containertools

   for measure in iterate_measures_forward_in_expr(expr):
      if len(measure) == 1:
         if isinstance(measure[0], Tuplet):
            tuplet = measure[0]
            tuplet_multiplier = tuplet.duration.multiplier
            tuplet_denominator = tuplet_multiplier.denominator
            reduced_denominator = mathtools.remove_powers_of_two(tuplet_denominator)
            meter = contexttools.get_effective_time_signature(measure)
            meter_rational = durtools.Duration(meter.numerator, meter.denominator)
            numerator = meter_rational.numerator * reduced_denominator
            denominator = meter_rational.denominator * reduced_denominator
            measure._attach_explicit_meter(numerator, denominator)
            meter_multiplier = contexttools.get_effective_time_signature(measure).multiplier
            written_adjustment = tuplet_multiplier / meter_multiplier
            componenttools.move_parentage_and_spanners_from_components_to_components(
               [tuplet], tuplet[:])
            containertools.scale_contents_of_container(measure, written_adjustment)
