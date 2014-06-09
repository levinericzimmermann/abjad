# -*- encoding: utf-8 -*-
import os
from abjad import *
import scoremanager
score_manager = scoremanager.ide.AbjadIDE(is_test=True)


def test_ScorePackageManager_invoke_shell_01():

    input_ = 'red~example~score !pwd q'
    score_manager._run(input_=input_)

    path = os.path.join(
        score_manager._configuration.example_score_packages_directory,
        'red_example_score',
        )
    string = '\n{}\n'.format(path)
    assert string in score_manager._transcript.contents