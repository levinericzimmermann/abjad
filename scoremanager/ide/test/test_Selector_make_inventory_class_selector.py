# -*- encoding: utf-8 -*-
from abjad import *
import scoremanager
session = scoremanager.ide.Session(is_test=True)


def test_Selector_make_inventory_class_selector_01():

    selector = scoremanager.ide.Selector(session=session)
    selector = selector.make_inventory_class_selector()
    input_ = 'markup'
    result = selector._run(input_=input_)

    assert result == markuptools.MarkupInventory