"""
Unit tests for Exercise 4.1-5.
"""

import pytest
from src.Chapter04.Exercise_4_1_5 import kadane_maximum_subarray


def test_known_case():
    arr = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    result = kadane_maximum_subarray(arr)
    assert result == (7, 10, 43)  # subarray [18, 20, -7, 12]


def test_single_element():
    arr = [-5]
    result = kadane_maximum_subarray(arr)
    assert result == (0, 0, -5)


def test_empty_array_raises():
    with pytest.raises(ValueError):
        kadane_maximum_subarray([])
