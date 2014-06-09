# -*- encoding: utf-8 -*-
import os
from abjad import *
import scoremanager
score_manager = scoremanager.ide.AbjadIDE(is_test=True)


def test_ScorePackageManager_edit_catalog_number_01():

    path = os.path.join(
        score_manager._configuration.example_score_packages_directory,
        'red_example_score',
        )
    metadata_path = os.path.join(path, '__metadata__.py')

    manager = scoremanager.ide.ScorePackageManager
    manager = manager(path=path, session=score_manager._session)
    assert manager._get_metadatum('catalog_number') == '#165'

    with systemtools.FilesystemState(keep=[metadata_path]):
        input_ = 'red~example~score p catalog~number for~foo~bar q'
        score_manager._run(input_=input_)
        session = scoremanager.ide.Session(is_test=True)
        manager = scoremanager.ide.ScorePackageManager
        manager = manager(path=path, session=session)
        assert manager._get_metadatum('catalog_number') == 'for foo bar'