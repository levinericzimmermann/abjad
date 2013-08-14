# -*- encoding: utf-8 -*-
from abjad.tools import componenttools
from abjad.tools import containertools
from abjad.tools import durationtools
from abjad.tools.selectiontools import more


def fuse_measures(measures):
    r'''Fuse selection of `measures`:

    ::

        >>> staff = \
        ...     Staff(measuretools.make_measures_with_full_measure_spacer_skips(
        ...     [(1, 8), (2, 16)]))
        >>> measuretools.fill_measures_in_expr_with_repeated_notes(
        ...     staff, Duration(1, 16))
        >>> pitchtools.set_ascending_named_diatonic_pitches_on_tie_chains_in_expr(staff)
        >>> spannertools.BeamSpanner(staff.select_leaves())
        BeamSpanner(c'16, d'16, e'16, f'16)

    ..  doctest::

        >>> f(staff)
        \new Staff {
            {
                \time 1/8
                c'16 [
                d'16
            }
            {
                \time 2/16
                e'16
                f'16 ]
            }
        }

    ::

        >>> measuretools.fuse_measures(staff[:])
        Measure(2/8, [c'16, d'16, e'16, f'16])

    ..  doctest::

        >>> f(staff)
        \new Staff {
            {
                \time 2/8
                c'16 [
                d'16
                e'16
                f'16 ]
            }
        }

    Return new measure.

    Allow parent-contiguous `measures`.

    Do not define measure fusion across intervening container boundaries.

    Calculate best new time signature.

    Instantiate new measure.

    Give `measures` contents to new measure.

    Give `measures` dominant spanners to new measure.

    Give `measures` parentage to new measure.

    Leave `measures` empty, unspanned and outside-of-score.

    Note that `measures` must be a selection.
    '''
    from abjad.tools import contexttools
    from abjad.tools import measuretools
    from abjad.tools import selectiontools
    from abjad.tools import timesignaturetools
    Selection = selectiontools.Selection

    # check input
    assert isinstance(measures, selectiontools.SliceSelection), repr(measures)
    assert Selection._all_are_contiguous_components_in_same_parent(
        measures, component_classes=(measuretools.Measure, ))

    # return none on empty measures
    if len(measures) == 0:
        return None

    # TODO: instantiate a new measure
    #       instead of returning a reference to existing measure
    if len(measures) == 1:
        return measures[0]

    parent, start, stop = measures._get_parent_and_start_stop_indices()
    old_denominators = []
    new_duration = durationtools.Duration(0)
    for measure in measures:
        effective_time_signature = measure.time_signature
        old_denominators.append(effective_time_signature.denominator)
        new_duration += effective_time_signature.duration

    new_time_signature = \
        timesignaturetools.duration_and_possible_denominators_to_time_signature(
        new_duration, old_denominators)

    music = []
    for measure in measures:
        # scale before reassignment to prevent tie chain scale drama
        signature = measure.time_signature
        prolation = signature.implied_prolation
        multiplier = prolation / new_time_signature.implied_prolation
        containertools.scale_contents_of_container(measure, multiplier)
        measure_music = measure[:]
        measure_music._set_parents(None)
        music += measure_music

    new_measure = measuretools.Measure(new_time_signature, music)

    if parent is not None:
        measures._give_dominant_spanners_to_components([new_measure])

    measures._set_parents(None)
    if parent is not None:
        parent.insert(start, new_measure)

    return new_measure
