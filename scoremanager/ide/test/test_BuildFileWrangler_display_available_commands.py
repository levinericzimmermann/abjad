# -*- encoding: utf-8 -*-
from abjad import *
import scoremanager
score_manager = scoremanager.ide.AbjadIDE(is_test=True)


def test_BuildFileWrangler_display_available_commands_01():
    
    input_ = 'red~example~score u ? q'
    score_manager._run(input_=input_)
    contents = score_manager._transcript.contents

    assert 'build files - available commands' in contents


def test_BuildFileWrangler_display_available_commands_02():
    
    input_ = 'u ? q'
    score_manager._run(input_=input_)
    contents = score_manager._transcript.contents

    assert 'Abjad IDE - build files - available commands' in contents