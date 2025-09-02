"""
Test for Exercise 2.1-3 (CLRS)

This test verifies that the `linear_search` function from
Exercise_2_1_3.py correctly implements the linear search algorithm.

Expected behavior:
- Returns the 0-based index of the first occurrence of the target value in the array.
- Returns None if the target value is not found.
"""

import pytest
from src.Chapter02.Exercise_2_1_3 import linear_search

def test_linear_search_found_and_not_found():
    # Prepare test data
    array = [31, 41, 59, 26, 41, 58]
    # Case 1: Target is the first element
    assert linear_search(array, 31) == 0
    # Case 2: Target appears multiple times — should return first occurrence
    assert linear_search(array, 41) == 1
    # Case 3: Target is the last element
    assert linear_search(array, 58) == len(array) - 1
    # Case 4: Target not in array — should return None
    assert linear_search(array, 100) is None
