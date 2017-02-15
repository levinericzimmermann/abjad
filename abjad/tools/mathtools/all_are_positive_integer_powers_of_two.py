# -*- coding: utf-8 -*-


def all_are_positive_integer_powers_of_two(argument):
    '''Is true when `argument` is an iterable collection of positive integer
    powers of two. Otherwise false.

    ..  container:: example

        ::

            >>> items = [1, 1, 1, 2, 4, 32, 32]
            >>> mathtools.all_are_nonnegative_integer_powers_of_two(items)
            True

        ::

            >>> mathtools.all_are_nonnegative_integer_powers_of_two(17)
            False

    ..  container:: example

        Is true when `argument` is empty:

        ::

            >>> mathtools.all_are_nonnegative_integer_powers_of_two([])
            True

    Returns true or false.
    '''
    from abjad.tools import mathtools
    try:
        return all(
            mathtools.is_positive_integer_power_of_two(_) for _ in argument
            )
    except TypeError:
        return False
