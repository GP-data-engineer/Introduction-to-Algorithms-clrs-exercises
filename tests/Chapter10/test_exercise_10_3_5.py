import pytest
from src.Chapter10.Exercise_10_3_5 import compactify_list

def test_compactify():
    L = {"key": [1, 2], "prev": [None, 0], "next": [1, None]}
    F = {"free": [2, 3]}
    L2, F2 = compactify_list(L, F, 4)
    assert F2["free"] == [2, 3]
    assert L2["prev"] == [None, 0]
