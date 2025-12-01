# Test for Exercise 9.3-4 (EN): Verifies partitioning around known i-th smallest element.
# Test do Exercise 9.3-4 (PL): Sprawdza podział względem znanego i-tego najmniejszego elementu.

import pytest
from src.Chapter09.Exercise_9_3_4 import extract_extremes_given_ith

def test_partition_correctness():
    A = [3, 2, 9, 0, 7, 5, 4, 8, 6, 1]
    ith_value = sorted(A)[4]  # 5th smallest
    smaller, equal, greater = extract_extremes_given_ith(A, ith_value)
    assert all(x < ith_value for x in smaller)
    assert all(x > ith_value for x in greater)
    assert equal == [ith_value]
