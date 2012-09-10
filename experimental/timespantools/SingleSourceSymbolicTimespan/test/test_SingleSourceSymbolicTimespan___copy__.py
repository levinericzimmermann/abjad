import copy
import fractions
from experimental import *


def test_SingleSourceSymbolicTimespan___copy___01():

    timespan_1 = timespantools.SingleSourceSymbolicTimespan(multiplier=fractions.Fraction(1, 3))
    timespan_2 = copy.deepcopy(timespan_1)

    assert isinstance(timespan_1, timespantools.SingleSourceSymbolicTimespan)
    assert isinstance(timespan_2, timespantools.SingleSourceSymbolicTimespan)
    assert not timespan_1 is timespan_2
    assert timespan_1 == timespan_2
