# -*- encoding: utf-8 -*-
import copy
import inspect
import pytest
from abjad import *
pytest.skip()


@pytest.mark.parametrize('klass', documentationtools.list_all_abjad_classes())
def test_copy_01(klass):
    r'''All objects with a storage format can copy.
    '''

    if '_storage_format' in dir(klass) and not inspect.isabstract(klass):
        instance_one = klass()
        instance_two = copy.copy(instance_one)
        assert instance_one == instance_two
