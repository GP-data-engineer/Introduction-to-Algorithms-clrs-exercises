"""
Testy do Problem 8-3 (PL): Sprawdzamy sortowanie liczb dziesiętnych i binarnych.
Tests for Problem 8-3 (EN): Verifies sorting of decimal and binary representations.
"""

import pytest
from src.Chapter08.Problem_8_3 import radix_sort_decimal, radix_sort_binary_strings

def test_radix_sort_decimal():
    arr = [123, 4, 56, 789, 1]
    sorted_arr = radix_sort_decimal(arr.copy())
    assert sorted_arr == sorted(arr)

def test_radix_sort_binary_strings():
    arr = ["101", "1", "1000", "011", "010"]
    sorted_arr = radix_sort_binary_strings(arr.copy())
    assert sorted_arr == sorted(arr)

def test_empty_decimal():
    assert radix_sort_decimal([]) == []

def test_empty_binary():
    assert radix_sort_binary_strings([]) == []
