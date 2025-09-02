"""
Test for Exercise 2.1-2 (CLRS)

This test verifies that the `insertion_sort_descending` function from
Exercise_2_1_2.py correctly implements the insertion sort algorithm
to sort an array in nonincreasing (descending) order.

Expected behavior:
- The returned list should be sorted in nonincreasing order.
- The output should match the expected sorted list for the given input.
"""

import pytest
from src.Chapter02.Exercise_2_1_2 import insertion_sort_descending

def test_insertion_sort_descending_fixed_array():
    # Input array
    data = [5, 2, 4, 6, 1, 3]
    # Expected sorted array in descending order
    expected = sorted(data, reverse=True)
    # Call the function
    result = insertion_sort_descending(data.copy())
    # Check if the result matches the expected sorted list
    assert result == expected, f"Expected {expected}, but got {result}"
    # Additional check: ensure the list is sorted in nonincreasing order
    assert all(result[i] >= result[i+1] for i in range(len(result)-1)), \
        "The list is not sorted in nonincreasing order."
