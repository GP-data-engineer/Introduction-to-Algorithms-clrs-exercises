# Test for Exercise 9.3.6 (EN): Verifies partitioning around known i-th smallest element.
# Test do Exercise 9.3.6 (PL): Sprawdza podział względem znanego i-tego najmniejszego elementu.

import pytest
from src.Chapter09.Exercise_9_3_6 import partition_by_known_element

def test_partition_correctness():
    A = [3, 2, 9, 0, 7, 5, 4, 8, 6, 1]
    pivot = sorted(A)[4]  # 5th smallest
    smaller, equal, greater = partition_by_known_element(A, pivot)
    assert all(x < pivot for x in smaller)
    assert all(x > pivot for x in greater)