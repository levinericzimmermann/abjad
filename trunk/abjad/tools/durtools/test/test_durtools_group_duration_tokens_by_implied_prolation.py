from abjad import *
from abjad.tools import durtools
import py.test


def test_durtools_group_duration_tokens_by_implied_prolation_01( ):
    assert py.test.raises(
        AssertionError, 'durtools.group_duration_tokens_by_implied_prolation([ ])')


def test_durtools_group_duration_tokens_by_implied_prolation_02( ):
    t = durtools.group_duration_tokens_by_implied_prolation([(1, 4)])
    assert t == [[(1, 4)]]


def test_durtools_group_duration_tokens_by_implied_prolation_03( ):
    t = durtools.group_duration_tokens_by_implied_prolation([(1, 4), (1, 4), (1, 8)])
    assert t == [[(1, 4), (1, 4), (1, 8)]]


def test_durtools_group_duration_tokens_by_implied_prolation_04( ):
    t = durtools.group_duration_tokens_by_implied_prolation([(1, 4), (1, 3), (1, 8)])
    assert t == [[(1, 4)], [(1, 3)], [(1, 8)]]


def test_durtools_group_duration_tokens_by_implied_prolation_05( ):
    t = durtools.group_duration_tokens_by_implied_prolation([(1, 4), (1, 2), (1, 3)])
    assert t == [[(1, 4), (1, 2)], [(1, 3)]]


def test_durtools_group_duration_tokens_by_implied_prolation_06( ):
    t = durtools.group_duration_tokens_by_implied_prolation([(1, 4), (1, 2), (1, 3), (1, 6),
        (1, 5)])
    assert t == [[(1, 4), (1, 2)], [(1, 3), (1, 6)], [(1, 5)]]


def test_durtools_group_duration_tokens_by_implied_prolation_07( ):
    t = durtools.group_duration_tokens_by_implied_prolation([(1, 24), (2, 24), (3, 24),
        (4, 24), (5, 24), (6, 24)])
    assert t == [[(1, 24), (2, 24), (3, 24), (4, 24), (5, 24), (6, 24)]]

