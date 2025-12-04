# Test for Exercise 9.3.7 (EN): Verifies correct range selection from sorted array.
# Test do Exercise 9.3.7 (PL): Sprawdza poprawność wyboru zakresu z posortowanej tablicy.

import pytest
from src.Chapter09.Exercise_9_3_7 import select_range

def test_range_selection():
    A = [3, 2, 9, 0, 7, 5, 4, 8, 6, 1]
    result = select_range(A, 3, 4)
    assert result == [2, 3, 4, 5]