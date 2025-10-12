import pytest
from src.Chapter07.Exercise_7_1_4 import quicksort_desc

def test_quicksort_desc():
    arr = [3, 6, 1, 8, 4]
    result = quicksort_desc(arr)
    assert result == sorted(arr, reverse=True)
