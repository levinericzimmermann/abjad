# -*- encoding: utf-8 -*-
import os
from abjad import *
import scoremanager
score_manager = scoremanager.ide.AbjadIDE(is_test=True)


def test_DistributionFileWrangler_copy_file_01():
    r'''In library: partial test because we can't be sure any user 
    score packages will be present. And because Score PackageManager allows 
    copying into user score packges only (because copying into example score 
    packages could pollute the example score packages).
    '''

    input_ = 'd cp red-example-score.pdf q'
    score_manager._run(input_=input_)
    contents = score_manager._transcript.contents

    titles = [
        'Abjad IDE - scores',
        'Abjad IDE - distribution files',
        'Abjad IDE - distribution files',
        ]
    assert score_manager._transcript.titles == titles
    assert 'Select storehouse:' in contents


def test_DistributionFileWrangler_copy_file_02():
    r'''In score package distribution directory.
    '''

    source_path = os.path.join(
        score_manager._configuration.example_score_packages_directory,
        'red_example_score',
        'distribution',
        'red-example-score.pdf',
        )
    target_path = os.path.join(
        score_manager._configuration.example_score_packages_directory,
        'red_example_score',
        'distribution',
        'copied-red-example-score.pdf',
        )

    with systemtools.FilesystemState(keep=[source_path], remove=[target_path]):
        input_ = 'red~example~score d cp'
        input_ += ' red-example-score.pdf copied-red-example-score.pdf y q'
        score_manager._run(input_=input_)
        contents = score_manager._transcript.contents
        assert os.path.exists(source_path)
        assert os.path.exists(target_path)
        assert 'copied-red-example-score.pdf' in contents