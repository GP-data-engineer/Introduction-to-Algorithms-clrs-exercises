import pytest 
from src.Chapter06.Exercise_6_2_4 import max_heapify_on_leaf

def test_max_heapify_on_leaf():
    assert "leaf" in max_heapify_on_leaf()
