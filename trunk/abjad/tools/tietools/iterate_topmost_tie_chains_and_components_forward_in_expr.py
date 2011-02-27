from abjad.components._Leaf import _Leaf
from abjad.components import Container
from abjad.exceptions import TieChainError
from abjad.tools import spannertools
from abjad.tools.tietools.get_tie_chain import get_tie_chain


def iterate_topmost_tie_chains_and_components_forward_in_expr(expr):
   r'''Yield the left-to-right, top-level contents of `expr`
   with chain-wrapped leaves. ::

      t = Staff(notetools.make_notes(0, [(5, 32)] * 4))
      t.insert(4, tuplettools.FixedDurationTuplet((2, 8), notetools.make_repeated_notes(3)))
      macros.diatonicize(t)
      abjad> f(t)
      \new Staff {
         c'8 ~
         c'32
         \times 2/3 {
            d'8
            e'8
            f'8
         }
         g'8 ~
         g'32
         a'8 ~
         a'32
         b'8 ~
         b'32
      }

   ::

      abjad> for x in tietools.iterate_topmost_tie_chains_and_components_forward_in_expr(t):
      ...     x
      ... 
      (Note(c', 8), Note(c', 32))
      (Note(d', 8), Note(d', 32))
      tuplettools.FixedDurationTuplet(1/4, [e'8, f'8, g'8])
      (Note(a', 8), Note(a', 32))
      (Note(b', 8), Note(b', 32))

   Crossing ties raise :exc:`TieChainError`.

   .. versionchanged:: 1.1.2
      renamed ``iterate.chained_contents( )`` to
      ``tietools.iterate_topmost_tie_chains_and_components_forward_in_expr( )``.

   .. versionchanged:: 1.1.2
      renamed ``iterate.topmost_tie_chains_and_components_forward_in_expr( )`` to
      ``tietools.iterate_topmost_tie_chains_and_components_forward_in_expr( )``.
   '''

   if isinstance(expr, _Leaf):
      if len(get_tie_chain(expr)) == 1:
         yield get_tie_chain(expr)
      else:
         raise TieChainError('can not have only one leaf in tie chain.')
   elif isinstance(expr, (list, Container)):
      for component in expr:
         if isinstance(component, _Leaf):
            tie_spanners = spannertools.get_all_spanners_attached_to_component(
               component, spannertools.TieSpanner)
            #if not component.tie.spanned or component.tie.last:
            if not tie_spanners or tuple(tie_spanners)[0]._is_my_last_leaf(component):
               yield get_tie_chain(component)
         elif isinstance(component, Container):
            yield component
   else:
      raise ValueError('input must be iterable.')
