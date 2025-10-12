import pytest 
from src.Chapter07.Exercise_7_1_1 import partition

def test_partition():
    arr = [13, 19, 9, 5, 12, 8, 7, 4, 21, 2, 6, 11]
    q, result = partition(arr, 0, len(arr)-1)
    pivot = result[q]
    assert all(x <= pivot for x in result[:q])
    assert all(x >= pivot for x in result[q+1:])
