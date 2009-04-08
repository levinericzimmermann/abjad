from abjad.tools import clone
from abjad.helpers.retroiterate import retroiterate
from abjad.leaf.leaf import _Leaf


def leaves_multiply(expr, total = 1):
   '''Insert n copies of each leaf l_i after l_i in expr.
      preserve parentage and spanners.'''

   for leaf in retroiterate(expr, _Leaf):
      leaf.splice(clone.unspan([leaf], total - 1))
