# Test for Exercise 9.3.9 (EN): Verifies median of two sorted arrays.
# Test do Exercise 9.3.9 (PL): Sprawdza medianę dwóch posortowanych tablic.

import pytest
from src.Chapter09.Exercise_9_3_9 import find_median_sorted_arrays

def test_median_even():
    X = [1, 3, 5, 7]
    Y = [2, 4, 6, 8]
    assert find_median_sorted_arrays(X, Y) == 4

def test_median_odd():
    X = [1, 3, 5]
    Y = [2, 4, 6]
    assert find_median_sorted_arrays(X, Y) == 3