# -*- encoding: utf-8 -*-
from abjad.tools import indicatortools
from abjad.tools import scoretools
from abjad.tools import selectiontools
from abjad.tools.topleveltools import iterate
from abjad.tools.quantizationtools.AttackPointOptimizer \
	import AttackPointOptimizer


class NaiveAttackPointOptimizer(AttackPointOptimizer):
    r'''Concrete ``AttackPointOptimizer`` subclass which optimizes
    attack points by fusing tie leaves within tie chains with
    leaf durations decreasing monotonically.

    ``TieChains`` will be partitioned into sub-``TieChains`` if
    leaves are found with ``TempoMarks`` attached.

    Return ``NaiveAttackPointOptimizer`` instance.
    '''

    ### SPECIAL METHODS ###

    def __call__(self, expr):
        for tie_chain in iterate(expr).by_tie_chain(reverse=True):
            sub_chains = []
            current_sub_chain = []
            for leaf in tie_chain:
                tempos = leaf._get_indicators(indicatortools.Tempo)
                if tempos:
                    if current_sub_chain:
                        current_sub_chain = \
                            selectiontools.TieChain(current_sub_chain)
                        sub_chains.append(current_sub_chain)
                    current_sub_chain = []
                current_sub_chain.append(leaf)
            if current_sub_chain:
                current_sub_chain = selectiontools.TieChain(current_sub_chain)
                sub_chains.append(current_sub_chain)
            for sub_chain in sub_chains:
                sub_chain._fuse_leaves_by_immediate_parent()
