import pytest 

from src.Chapter06.Exercise_6_2_1 import max_heapify_example

def test_max_heapify_example():
    result = max_heapify_example()
    assert result[2] == 16
    assert result[8] == 3
