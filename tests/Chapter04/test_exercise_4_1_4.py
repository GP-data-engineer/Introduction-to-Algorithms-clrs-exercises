"""
Unit tests for Exercise 4.1-4.
"""

import pytest
from src.Chapter04.Exercise_4_1_4 import max_subarray_allow_empty


def test_all_negative_returns_empty():
    arr = [-5, -1, -8]
    result = max_subarray_allow_empty(arr)
    assert result == (-1, -1, 0)


def test_mixed_numbers():
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    result = max_subarray_allow_empty(arr)
    assert result == (3, 6, 6)  # subarray [4, -1, 2, 1]


def test_empty_array():
    assert max_subarray_allow_empty([]) == (-1, -1, 0)
