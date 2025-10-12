import pytest
from src.Chapter07.Exercise_7_1_2 import partition_equal

def test_partition_equal():
    arr = [5, 5, 5, 5]
    q, _ = partition_equal(arr, 0, len(arr)-1)
    assert q == (0 + len(arr)-1)//2
