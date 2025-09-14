"""
Unit tests for Exercise 4.1-2.
"""

import pytest
from src.Chapter04.Exercise_4_1_2 import brute_force_maximum_subarray


def test_brute_force():
    arr = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    result = brute_force_maximum_subarray(arr)
    assert result == (7, 10, 43)  # known correct result


def test_empty_array():
    with pytest.raises(ValueError):
        brute_force_maximum_subarray([])
