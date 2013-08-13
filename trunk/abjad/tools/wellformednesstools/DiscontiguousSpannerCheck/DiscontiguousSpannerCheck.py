# -*- encoding: utf-8 -*-
from abjad.tools import componenttools
from abjad.tools import spannertools
from abjad.tools.wellformednesstools.Check import Check


class DiscontiguousSpannerCheck(Check):
    r'''There are now two different types of spanner.
    Most spanners demand that spanner components be thread-contiguous.
    But a few special spanners (like Tempo) do not make such a demand.
    The check here consults the experimental `_contiguity_constraint`.
    '''

    def _run(self, expr):
        violators = []
        total, bad = 0, 0
        for spanner in \
            spannertools.get_spanners_attached_to_any_improper_child_of_component(
            expr):
            if spanner._contiguity_constraint == 'thread':
                if not componenttools.all_are_logical_voice_contiguous_components(
                    spanner[:]):
                    violators.append(spanner)
            total += 1
        return violators, total
