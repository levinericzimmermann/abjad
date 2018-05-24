import abjad


def test_spannertools_Beam__is_beamable_01():
    """
    Eighth notes are beamable.
    Quarter notes are not beamable.
    """

    assert abjad.Beam._is_beamable(abjad.Note(0, (1, 8)))
    assert not abjad.Beam._is_beamable(abjad.Note("c'4"))


def test_spannertools_Beam__is_beamable_02():
    """
    Containers are not beamable.
    """

    assert not abjad.Beam._is_beamable(abjad.Staff([]))
