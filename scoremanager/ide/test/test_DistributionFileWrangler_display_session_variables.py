# -*- encoding: utf-8 -*-
from abjad import *
import scoremanager
score_manager = scoremanager.ide.AbjadIDE(is_test=True)


def test_DistributionFileWrangler_display_session_variables_01():
    
    input_ = 'red~example~score d sv q'
    score_manager._run(input_=input_)
    contents = score_manager._transcript.contents

    assert 'command_history' in contents
    assert 'controller_stack' in contents


def test_DistributionFileWrangler_display_session_variables_02():
    
    input_ = 'd sv q'
    score_manager._run(input_=input_)
    contents = score_manager._transcript.contents

    assert 'command_history' in contents
    assert 'controller_stack' in contents