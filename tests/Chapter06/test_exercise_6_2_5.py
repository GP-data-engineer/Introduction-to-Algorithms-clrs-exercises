import pytest
from src.Chapter06.Exercise_6_2_5 import max_heapify_iter

def test_max_heapify_iter():
    arr = [3, 17, 10, 1, 5]
    result = max_heapify_iter(arr, 0, len(arr))
    assert result[0] == 17
