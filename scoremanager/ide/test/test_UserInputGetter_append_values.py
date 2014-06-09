# -*- encoding: utf-8 -*-
from abjad import *
import scoremanager
session = scoremanager.ide.Session()


def test_UserInputGetter_append_values_01():

    getter = scoremanager.ide.UserInputGetter(session=session)
    getter.append_integer('attribute')
    input_ = 'foo -99'
    assert getter._run(input_=input_) == -99

    getter = scoremanager.ide.UserInputGetter(session=session)
    getter.append_integer_in_range('attribute', 1, 10)
    input_ = 'foo -99 99 7'
    assert getter._run(input_=input_) == 7

    getter = scoremanager.ide.UserInputGetter(session=session)
    menu_entries = ['apple', 'banana', 'cherry', 'durian', 'endive', 'fennel']
    section = scoremanager.ide.MenuSection(
        is_numbered=True,
        menu_entries=menu_entries,
        name='test',
        )
    getter.append_menu_section_range('attribute', section)
    result = [6, 5, 4, 1, 3]
    input_ = 'fen-dur, app, che'
    assert getter._run(input_=input_) == result

    getter = scoremanager.ide.UserInputGetter(session=session)
    getter.append_markup('attribute')
    input_ = 'foo'
    assert getter._run(input_=input_) == markuptools.Markup('foo')

    getter = scoremanager.ide.UserInputGetter(session=session)
    getter.append_named_pitch('attribute')
    input_ = "cs'"
    assert getter._run(input_=input_) == NamedPitch("cs'")

    getter = scoremanager.ide.UserInputGetter(session=session)
    getter.append_string('attribute')
    input_ = 'None -99 99 1-4 foo'
    assert getter._run(input_=input_) == 'foo'

    getter = scoremanager.ide.UserInputGetter(session=session)
    getter.append_string_or_none('attribute')
    input_ = '-99 99 1-4 None'
    assert getter._run(input_=input_) is None