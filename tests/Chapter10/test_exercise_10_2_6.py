import pytest
from src.Chapter10.Exercise_10_2_6 import SetList

def test_union_sets():
    s1 = SetList()
    s2 = SetList()
    s1.insert(10)
    s2.insert(20)
    s1.union(s2)
    assert s1.to_list() == [10, 20]
    assert s2.to_list() == []
