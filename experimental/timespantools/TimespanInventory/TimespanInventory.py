from abjad.tools.datastructuretools.ObjectInventory import ObjectInventory


class TimespanInventory(ObjectInventory):
    r'''.. versionadded:: 1.0

    ::

        >>> from experimental import *

    SymbolicTimespan inventory::

        >>> timespan_inventory = timespantools.TimespanInventory()

    ::

        >>> timespan_inventory.append(timespantools.TimespanConstant(0, 3))
        >>> timespan_inventory.append(timespantools.TimespanConstant(3, 6))
        >>> timespan_inventory.append(timespantools.TimespanConstant(6, 10))

    ::

        >>> z(timespan_inventory)
        timespantools.TimespanInventory([
            timespantools.TimespanConstant(
                start_offset=durationtools.Offset(0, 1),
                stop_offset=durationtools.Offset(3, 1)
                ),
            timespantools.TimespanConstant(
                start_offset=durationtools.Offset(3, 1),
                stop_offset=durationtools.Offset(6, 1)
                ),
            timespantools.TimespanConstant(
                start_offset=durationtools.Offset(6, 1),
                stop_offset=durationtools.Offset(10, 1)
                )
            ])

    SymbolicTimespan inventory.
    '''

    ### INITIALIZER ###

    def __init__(self, *args, **kwargs):
        ObjectInventory.__init__(self, *args, **kwargs)

    ### PUBLIC METHODS ###

    def get_timespan_that_satisfies_inequality(self, timespan_inequality):
        r'''Get timespan that satisifies `timespan_inequality`::

            >>> timespan_1 = timespantools.expr_to_timespan((2, 5))
            >>> timespan_inequality = timespaninequalitytools.timespan_2_starts_during_timespan_1(
            ...     timespan_1=timespan_1)

        ::

            >>> timespan_inventory.get_timespan_that_satisfies_inequality(timespan_inequality)
            TimespanConstant(start_offset=Offset(3, 1), stop_offset=Offset(6, 1))

        Return timespan when timespan inventory contains exactly one timespan
        that satisfies `timespan_inequality`.

        Raise exception when timespan inventory contains no timespan
        that satisfies `timespan_inequality`.

        Raise exception when timespan inventory contains more than one timespan
        that satisfies `timespan_inequality`.
        '''
        timespans = self.get_timespans_that_satisfy_inequality(timespan_inequality)
        if len(timespans) == 1:
            return timespans[0]
        elif 1 < len(timespans):
            raise Exception('extra timespan error.')
        else:
            raise Exception('missing timespan error.')

    def get_timespans_that_satisfy_inequality(self, timespan_inequality):
        r'''Get timespans that satisfy `timespan_inequality`::

            >>> timespan_1 = timespantools.expr_to_timespan((2, 8))
            >>> timespan_inequality = timespaninequalitytools.timespan_2_starts_during_timespan_1(
            ...     timespan_1=timespan_1)

        ::

            >>> timespans = timespan_inventory.get_timespans_that_satisfy_inequality(timespan_inequality)

        ::

            >>> for timespan in timespans:
            ...     timespan
            TimespanConstant(start_offset=Offset(3, 1), stop_offset=Offset(6, 1))
            TimespanConstant(start_offset=Offset(6, 1), stop_offset=Offset(10, 1))

        Return list of ``0`` or more timespans.
        '''
        result = []
        for timespan in self:
            if timespan_inequality(timespan_2=timespan):
                result.append(timespan)
        return result

    def has_timespan_that_satisfies_inequality(self, timespan_inequality):
        r'''True when timespan inventory has timespan that satisfies `timespan_inequality`::

            >>> timespan_1 = timespantools.expr_to_timespan((2, 8))
            >>> timespan_inequality = timespaninequalitytools.timespan_2_starts_during_timespan_1(
            ...     timespan_1=timespan_1)

        ::

            >>> timespan_inventory.has_timespan_that_satisfies_inequality(timespan_inequality)
            True

        Otherwise false::

            >>> timespan_1 = timespantools.expr_to_timespan((10, 20))
            >>> timespan_inequality = timespaninequalitytools.timespan_2_starts_during_timespan_1(
            ...     timespan_1=timespan_1)

        ::

            >>> timespan_inventory.has_timespan_that_satisfies_inequality(timespan_inequality)
            False

        Return boolean.
        '''
        return bool(self.get_timespans_that_satisfy_inequality(timespan_inequality))
