


import pytest
from src.Chapter10.Exercise_10_2_5 import CyclicListDict

def test_insert_search():
    d = CyclicListDict()
    d.insert(1)
    d.insert(2)
    assert d.search(2).key == 2

def test_delete():
    d = CyclicListDict()
    d.insert(5)
    d.insert(6)
    d.delete(5)
    assert d.search(5) is None
