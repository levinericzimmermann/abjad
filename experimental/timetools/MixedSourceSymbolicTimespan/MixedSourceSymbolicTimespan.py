from abjad.tools import abctools
from experimental.timetools.SymbolicTimespan import SymbolicTimespan


class MixedSourceSymbolicTimespan(SymbolicTimespan):
    r'''.. versionadded:: 1.0

    Mixed-source timespan.

        >>> from experimental import *

    Mixed-source timespan starting at the left edge of the last measure in the segment 
    with name ``'red'`` and stopping at the right edge of the first measure in the segment 
    with name ``'blue'``::

        >>> segment_selector = selectortools.SingleSegmentSelector(identifier='red')
        >>> inequality = timetools.timespan_2_starts_during_timespan_1(timespan_1=segment_selector.timespan)
        >>> measure_selector = selectortools.BackgroundMeasureSelector(inequality=inequality, start_identifier=-1)
        >>> start_timepoint = timetools.SymbolicTimepoint(selector=measure_selector)

    ::

        >>> segment_selector = selectortools.SingleSegmentSelector(identifier='blue')
        >>> inequality = timetools.timespan_2_starts_during_timespan_1(timespan_1=segment_selector.timespan)
        >>> measure_selector = selectortools.BackgroundMeasureSelector(inequality=inequality, stop_identifier=1)
        >>> stop_timepoint = timetools.SymbolicTimepoint(selector=measure_selector, edge=Right)
        
    ::

        >>> timespan = timetools.MixedSourceSymbolicTimespan(
        ... start_timepoint=start_timepoint, stop_timepoint=stop_timepoint)

    ::

        >>> z(timespan)
        timetools.MixedSourceSymbolicTimespan(
            start_timepoint=timetools.SymbolicTimepoint(
                selector=selectortools.BackgroundMeasureSelector(
                    inequality=timetools.TimespanInequality(
                        'timespan_1.start <= timespan_2.start < timespan_1.stop',
                        timespan_1=timetools.SingleSourceSymbolicTimespan(
                            selector=selectortools.SingleSegmentSelector(
                                identifier='red'
                                )
                            )
                        ),
                    start_identifier=-1
                    )
                ),
            stop_timepoint=timetools.SymbolicTimepoint(
                selector=selectortools.BackgroundMeasureSelector(
                    inequality=timetools.TimespanInequality(
                        'timespan_1.start <= timespan_2.start < timespan_1.stop',
                        timespan_1=timetools.SingleSourceSymbolicTimespan(
                            selector=selectortools.SingleSegmentSelector(
                                identifier='blue'
                                )
                            )
                        ),
                    stop_identifier=1
                    ),
                edge=Right
                )
            )

    Mixed-source timespan properties are read-only.
    '''

    ### INITIALIZER ###

    def __init__(self, start_timepoint=None, stop_timepoint=None):
        from experimental import timetools
        assert isinstance(start_timepoint, (timetools.SymbolicTimepoint, type(None))), repr(start_timepoint)
        assert isinstance(stop_timepoint, (timetools.SymbolicTimepoint, type(None))), repr(stop_timepoint)
        SymbolicTimespan.__init__(self)
        self._start_timepoint = start_timepoint
        self._stop_timepoint = stop_timepoint

    ### SPECIAL METHODS ###

    def __eq__(self, expr):
        '''True when `expr` equals self. Otherwise false.

        Return boolean.
        '''
        if isintance(expr, type(self)):
            if self.start_timepoint == timespan_2.start_timepoint:
                if self.stop_timepoint == timespan_2.stop_timepoint:
                    return True
        return False

    ### READ-ONLY PUBLIC PROPERTIES ###

    @property
    def start_timepoint(self):
        '''Mixed-source timespan start timepoint specified by user.

        Return timepoint or none.
        '''
        return self._start_timepoint

    @property
    def stop_timepoint(self):
        '''Mixed-source timepsan stop timepoint specified by user.

        Return timepoint or none.
        '''
        return self._stop_timepoint

    ### PUBLIC METHODS ###

    def get_score_start_offset(self, score_specification, context_name):
        '''Evaluate score start offset of symbolic timespan when applied
        to `context_name` in `score_specification`.

        .. note:: not yet implemented.

        Return offset.
        '''
        raise NotImplementedError

    def get_score_stop_offset(self, score_specification, context_name):
        '''Evaluate score stop offset of symbolic timespan when applied
        to `context_name` in `score_specification`.

        .. note:: not yet implemented.

        Return offset.
        '''
        raise NotImplementedError

    def set_segment_identifier(self, segment_identifier):
        '''.. note:: not yet implemented.
        '''
        raise NotImplementedError
