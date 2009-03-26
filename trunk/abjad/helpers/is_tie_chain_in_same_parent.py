from abjad.helpers.is_tie_chain import _is_tie_chain
from abjad.helpers.assess_components import assess_components


def _is_tie_chain_in_same_parent(expr):
   r'''True when expr is a tie chain with all leaves in same parent.
      IE, True when tie chain crosses no container boundaries.
      Otherwise False.

      Example:

      t = Staff(RigidMeasure((2, 8), run(2)) * 2)
      Tie(t.leaves[1:3])

      \new Staff {
            \time 2/8
            c'8
            c'8 ~
            \time 2/8
            c'8
            c'8
      }

      assert _is_tie_chain_in_same_parent(t.leaves[0].tie.chain)
      assert not _is_tie_chain_in_same_parent(t.leaves[1].tie.chain)
      assert not _is_tie_chain_in_same_parent(t.leaves[2].tie.chain)
      assert _is_tie_chain_in_same_parent(t.leaves[3].tie.chain)'''

   return _is_tie_chain(expr) and \
      assess_components(list(expr), share = 'parent')
