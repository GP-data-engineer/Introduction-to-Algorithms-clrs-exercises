"""
Testy do Problem 8-2 (PL): Sprawdzamy sortowanie binarne w miejscu.
Tests for Problem 8-2 (EN): Verifies in-place binary sorting.
"""

import pytest
from src.Chapter08.Problem_8_2 import in_place_binary_sort

def test_binary_sort_correctness():
    arr = [1, 0, 1, 0, 0, 1]
    sorted_arr = in_place_binary_sort(arr.copy())
    assert sorted_arr == [0, 0, 0, 1, 1, 1]

def test_all_zeros():
    arr = [0, 0, 0]
    assert in_place_binary_sort(arr.copy()) == [0, 0, 0]

def test_all_ones():
    arr = [1, 1, 1]
    assert in_place_binary_sort(arr.copy()) == [1, 1, 1]

def test_empty():
    assert in_place_binary_sort([]) == []
