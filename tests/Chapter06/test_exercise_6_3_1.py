import pytest
from src.Chapter06.Exercise_6_3_1 import build_max_heap

def test_build_max_heap():
    arr = [5, 3, 17, 10, 84, 19, 6, 22, 9]
    result = build_max_heap(arr)
    # Root should be the maximum
    assert result[0] == max(result)
    # Heap property check
    for i in range(len(result)//2):
        l, r = 2*i+1, 2*i+2
        if l < len(result):
            assert result[i] >= result[l]
        if r < len(result):
            assert result[i] >= result[r]
