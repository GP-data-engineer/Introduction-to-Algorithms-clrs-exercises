import pytest
from src.Chapter06.Exercise_6_4_1 import heapsort

def test_heapsort():
    arr = [5, 13, 2, 25, 7, 17, 20, 8, 4]
    result = heapsort(arr)
    assert result == sorted([5, 13, 2, 25, 7, 17, 20, 8, 4])
