import os
from experimental import *

scf_object = scoremanagementtools.core.ScoreManagementObject()


def test_ScoreManagementObject_package_importable_name_to_path_name_01():

    assert scf_object.package_importable_name_to_path_name('materials') == os.environ.get('SCORE_MANAGEMENT_TOOLS_MATERIALS_PATH')
    assert scf_object.package_importable_name_to_path_name('sketches') == os.environ.get('SCORE_MANAGEMENT_TOOLS_CHUNKS_PATH')
    assert scf_object.package_importable_name_to_path_name('specifiers') == os.environ.get('SCORE_MANAGEMENT_TOOLS_SPECIFIERS_PATH')
