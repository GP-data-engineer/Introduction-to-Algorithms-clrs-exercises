"""
Test for Problem 2.2 (CLRS) — Bubble Sort

This test verifies that the `bubble_sort` function from Problem_2_2.py
correctly sorts lists in nondecreasing order.

Expected behavior:
- Returns the sorted list in nondecreasing order.
- Works for empty lists, single-element lists, lists with duplicates,
  and lists containing negative numbers.
"""

import pytest
from src.Chapter02.Problem_2_2 import bubble_sort

@pytest.mark.parametrize("original", [
    [],                              # Empty list
    [1],                             # Single element
    [2, 1],                          # Two elements, unsorted
    [3, 2, 1],                       # Reverse order
    [5, 1, 4, 2, 8, 5, 2],           # List with duplicates
    [0, -1, -1, 3, 2, 2, 2, 1],      # List with negative numbers and duplicates
])
def test_bubble_sort_various_cases(original):
    """
    Test that bubble_sort correctly sorts various types of lists.
    """
    expected = sorted(original)
    arr_copy = list(original)

    result = bubble_sort(arr_copy)

    # Check that the sorted array matches the expected sorted list
    assert result == expected, f"For input {original}, expected {expected}, got {result}"

    # Ensure the result is sorted in nondecreasing order
    assert all(result[i] <= result[i+1] for i in range(len(result)-1)), \
        f"Result {result} is not sorted in nondecreasing order."
