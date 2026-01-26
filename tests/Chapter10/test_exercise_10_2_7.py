import pytest
from src.Chapter10.Exercise_10_2_7 import SinglyList

def test_reverse_list():
    l = SinglyList()
    for i in [1, 2, 3]:
        l.insert(i)
    l.reverse()
    assert l.to_list() == [1, 2, 3]
