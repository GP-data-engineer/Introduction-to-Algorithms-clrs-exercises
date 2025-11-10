"""
Testy do Problem 8.5 (PL): Sprawdzamy poprawność k-sortowania.
Tests for Problem 8.5 (EN): Verifies correctness of k-sorting.
"""

import pytest
from src.Chapter08.Problem_8_5 import k_sort, is_k_sorted

def test_k_sorted_property():
    arr = [10, 3, 5, 7, 2, 8]
    k = 2
    sorted_arr = k_sort(arr, k)
    assert is_k_sorted(sorted_arr, k)

def test_k_sort_length():
    arr = [4, 1, 3, 2]
    k = 2
    sorted_arr = k_sort(arr, k)
    assert len(sorted_arr) == len(arr)

def test_k_sort_identity():
    arr = [1, 2, 3, 4, 5]
    k = 1
    sorted_arr = k_sort(arr, k)
    assert sorted_arr == sorted(arr)
