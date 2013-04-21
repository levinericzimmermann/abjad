import os
from experimental import *


def test_ExgDirectoryProxy_01():

    exg_proxy = scoremanagementtools.proxies.ExgDirectoryProxy('example_score_1')

    assert exg_proxy.path_name == os.path.join(os.environ.get('SCORES'), 'example_score_1', 'exg')
    assert exg_proxy.source_file_name == \
        os.path.join(os.environ.get('SCORE_MANAGEMENT_TOOLS_PATH'), 'proxies', 'ExgDirectoryProxy', 'ExgDirectoryProxy.py')
    assert exg_proxy.spaced_class_name == 'exg directory proxy'
