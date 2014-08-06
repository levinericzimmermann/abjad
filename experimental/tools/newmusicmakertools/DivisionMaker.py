# -*- encoding: utf-8 -*-
from abjad.tools import durationtools
from abjad.tools import mathtools
from abjad.tools import sequencetools
from abjad.tools.abctools.AbjadValueObject import AbjadValueObject


class DivisionMaker(AbjadValueObject):
    r'''Division-maker.

    ..  container:: example

        ::

            >>> maker = newmusicmakertools.DivisionMaker(pattern=[(1, 4)])

        ::

            >>> print(format(maker, 'storage'))
            newmusicmakertools.DivisionMaker(
                cyclic=True,
                pattern=(
                    mathtools.NonreducedFraction(1, 4),
                    ),
                remainder=Right,
                )

    Object model of a partially evaluated function that accepts duration as
    input and returns nonreduced fractions as output.

    Follows the two-step configure-once / call-repeatedly pattern established
    by the rhythm-makers.
    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        '_cyclic',
        '_pattern',
        '_remainder',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        cyclic=True,
        pattern=None,
        remainder=Right,
        ):
        assert isinstance(cyclic, bool), repr(cyclic)
        self._cyclic = cyclic
        if pattern is not None:
            pattern_ = []
            for division in pattern:
                division = mathtools.NonreducedFraction(division)
                pattern_.append(division)
            pattern = tuple(pattern_)
        self._pattern = pattern
        if not remainder is None:
            assert remainder in (Left, Right), repr(remainder)
        self._remainder = remainder

    ### SPECIAL METHODS ###

    def __call__(self, division):
        r'''Calls maker on `division`.

        ..  container:: example

            Calls maker on division with no remainder:

            ::

                >>> maker = newmusicmakertools.DivisionMaker(pattern=[(1, 4)])
                >>> divisions = maker((3, 4))
                >>> for division in divisions:
                ...     division
                NonreducedFraction(1, 4)
                NonreducedFraction(1, 4)
                NonreducedFraction(1, 4)

        ..  container:: example

            Calls maker on division with remainder:

            ::

                >>> maker = newmusicmakertools.DivisionMaker(pattern=[(1, 4)])
                >>> divisions = maker((7, 8))
                >>> for division in divisions:
                ...     division 
                NonreducedFraction(1, 4)
                NonreducedFraction(1, 4)
                NonreducedFraction(1, 4)
                NonreducedFraction(1, 8)

            Positions remainder at right of output because maker `remainder`
            defaults to right.

        ..  container:: example

            Calls maker on zero division:

            ::

                >>> maker = newmusicmakertools.DivisionMaker(pattern=[(1, 4)])
                >>> maker(0)
                []

            Returns empty list.

        Returns possibly empty list of nonreduced fractions.
        '''
        input_division = mathtools.NonreducedFraction(division)
        input_duration = durationtools.Duration(input_division)
        if not self.pattern:
            return []
        divisions = list(self.pattern)
        if self.cyclic:
            divisions = sequencetools.repeat_sequence_to_weight(
                divisions,
                input_division,
                allow_total=Less,
                )
        total_duration = durationtools.Duration(sum(divisions))
        if total_duration == input_duration:
            return divisions
        if self.remainder is None:
            message = 'can not fill {} from {} exactly.'
            message = message.format(input_division, self.divisions)
            raise Exception(message)
        remainder = input_division - total_duration
        remainder = durationtools.Duration(remainder)
        remainder = mathtools.NonreducedFraction(remainder)
        if self.remainder is Left:
            divisions.insert(0, remainder)
        elif self.remainder is Right:
            divisions.append(remainder)
        else:
            raise ValueError(self.remainder)
        total_duration = durationtools.Duration(sum(divisions))
        pair = total_duration, input_duration
        assert total_duration == input_duration, pair
        return divisions

    ### PUBLIC PROPERTIES ###

    @property
    def cyclic(self):
        r'''Is true when maker reads divisions cyclically.
        Otherwise false.

        ..  container:: example

            ::

                >>> maker.cyclic
                True

        Returns boolean.
        '''
        return self._cyclic

    @property
    def pattern(self):
        r'''Gets maker pattern.

        ..  container:: example

            ::

                >>> maker.pattern
                (NonreducedFraction(1, 4),)

        Returns possibly empty tuple of positive nonreduced fractions.
        '''
        return self._pattern

    @property
    def remainder(self):
        r'''Gets direction at which any remainder will be positioned.

        ..  container:: example

            Positions remainder to right of noncyclic pattern:

            ::

                >>> maker = newmusicmakertools.DivisionMaker(
                ...     cyclic=False,
                ...     pattern=[(4, 16), (1, 16)],
                ...     remainder=Right,
                ...     )
                >>> divisions = maker(Duration(3, 4))
                >>> for division in divisions:
                ...     division
                NonreducedFraction(4, 16)
                NonreducedFraction(1, 16)
                NonreducedFraction(7, 16)

        ..  container:: example

            Positions remainder to right of cyclic pattern:

            ::

                >>> maker = newmusicmakertools.DivisionMaker(
                ...     cyclic=True,
                ...     pattern=[(4, 16), (1, 16)],
                ...     remainder=Right,
                ...     )
                >>> divisions = maker(Duration(3, 4))
                >>> for division in divisions:
                ...     division
                NonreducedFraction(4, 16)
                NonreducedFraction(1, 16)
                NonreducedFraction(4, 16)
                NonreducedFraction(1, 16)
                NonreducedFraction(1, 8)

        ..  container:: example

            Positions remainder to left of noncyclic pattern:

            ::

                >>> maker = newmusicmakertools.DivisionMaker(
                ...     cyclic=False,
                ...     pattern=[(1, 4), (1, 16)],
                ...     remainder=Left,
                ...     )
                >>> divisions = maker(Duration(3, 4))
                >>> for division in divisions:
                ...     division
                NonreducedFraction(7, 16)
                NonreducedFraction(1, 4)
                NonreducedFraction(1, 16)

        ..  container:: example

            Positions remainder to left of cyclic pattern:

            ::

                >>> maker = newmusicmakertools.DivisionMaker(
                ...     cyclic=True,
                ...     pattern=[(1, 4), (1, 16)],
                ...     remainder=Left,
                ...     )
                >>> divisions = maker(Duration(3, 4))
                >>> for division in divisions:
                ...     division
                NonreducedFraction(1, 8)
                NonreducedFraction(1, 4)
                NonreducedFraction(1, 16)
                NonreducedFraction(1, 4)
                NonreducedFraction(1, 16)

        Returns left, right or none.
        '''
        return self._remainder