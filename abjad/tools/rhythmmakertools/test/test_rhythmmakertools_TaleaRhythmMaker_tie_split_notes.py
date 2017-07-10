# -*- coding: utf-8 -*-
import abjad
from abjad import *


def test_rhythmmakertools_TaleaRhythmMaker_tie_split_notes_01():

    talea = rhythmmakertools.Talea(
        counts=[5],
        denominator=16,
        )
    rhythm_maker = rhythmmakertools.TaleaRhythmMaker(
        talea=talea,
        )

    divisions = [(2, 8), (2, 8), (2, 8), (2, 8)]
    selections = rhythm_maker(divisions)

    selections = Sequence(selections).flatten()
    maker = abjad.MeasureMaker()
    measures = maker(divisions)
    staff = Staff(measures)
    measures = mutate(staff).replace_measure_contents(selections)

    assert format(staff) == String.normalize(
        r'''
        \new Staff {
            {
                \time 2/8
                c'4 ~
            }
            {
                c'16 [
                c'8. ~ ]
            }
            {
                c'8 [
                c'8 ~ ]
            }
            {
                c'8. [
                c'16 ]
            }
        }
        '''
        )

    assert inspect(staff).is_well_formed()


def test_rhythmmakertools_TaleaRhythmMaker_tie_split_notes_02():

    talea = rhythmmakertools.Talea(
        counts=[5],
        denominator=16,
        )
    rhythm_maker = rhythmmakertools.TaleaRhythmMaker(
        talea=talea,
        )

    divisions = [(3, 16), (5, 8), (4, 8), (7, 16)]
    selections = rhythm_maker(divisions)

    selections = Sequence(selections).flatten()
    maker = abjad.MeasureMaker()
    measures = maker(divisions)
    staff = Staff(measures)
    measures = mutate(staff).replace_measure_contents(selections)

    assert format(staff) == String.normalize(
        r'''
        \new Staff {
            {
                \time 3/16
                c'8. ~
            }
            {
                \time 5/8
                c'8
                c'4 ~
                c'16 [
                c'8. ~ ]
            }
            {
                \time 4/8
                c'8
                c'4 ~
                c'16 [
                c'16 ~ ]
            }
            {
                \time 7/16
                c'4
                c'8.
            }
        }
        '''
        )

    assert inspect(staff).is_well_formed()
