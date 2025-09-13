"""
Unit tests for Exercise 4.1-1.
"""

import pytest
from src.Chapter04.Exercise_4_1_1 import find_maximum_subarray_all_negative


def test_all_negative():
    arr = [-5, -9, -3, -8]
    result = find_maximum_subarray_all_negative(arr)
    assert result == (2, 2, -3)


def test_empty_array():
    with pytest.raises(ValueError):
        find_maximum_subarray_all_negative([])
