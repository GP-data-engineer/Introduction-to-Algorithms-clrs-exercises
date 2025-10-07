import pytest 
from src.Chapter06.Exercise_6_2_2 import min_heapify

def test_min_heapify():
    arr = [5, 3, 4]
    result = min_heapify(arr, 0, len(arr))
    assert result[0] == 3
