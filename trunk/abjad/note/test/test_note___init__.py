from abjad import *
from py.test import raises


def test_note___init___01( ):
   '''Init note with pitch in octave zero.'''
   t = Note(-37, (1, 4))
   assert t.format == 'b,,,4'


def test_note___init__02( ):
   '''Init note with non-assignable duration.'''
   raises(AssignabilityError, 'Note(0, (5, 8))')


def test_note___init__03( ):
   '''Init note with LilyPond-style pitch string.'''
   t = Note('c,,', (1, 4))
   assert t.format == 'c,,4'
