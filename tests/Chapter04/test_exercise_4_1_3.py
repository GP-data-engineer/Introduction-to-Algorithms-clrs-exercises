"""
Unit tests for Exercise 4.1-3.
"""

import pytest
from src.Chapter04.Exercise_4_1_3 import brute_force_maximum_subarray, recursive_maximum_subarray, find_crossover_point


def test_algorithms_same_result():
    arr = [2, -1, 2, 3, -9, 5]
    bf_result = brute_force_maximum_subarray(arr)
    rec_result = recursive_maximum_subarray(arr, 0, len(arr) - 1)
    assert bf_result[2] == rec_result[2]  # compare sums


def test_crossover_point():
    n0 = find_crossover_point(50)
    assert isinstance(n0, int)
    assert n0 == -1 or n0 >= 2
