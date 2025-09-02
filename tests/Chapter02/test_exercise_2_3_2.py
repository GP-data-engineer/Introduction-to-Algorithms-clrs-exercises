"""
Test for Exercise 2.3-2 (CLRS)

This test verifies that the `merge_sort_no_sentinels` function from
Exercise_2_3_2.py correctly implements merge sort without using sentinel values.

Expected behavior:
- Sorts the list in nondecreasing order in place.
- Works for empty lists, single-element lists, lists with duplicates,
  and lists containing negative numbers.
"""

import pytest
from src.Chapter02.Exercise_2_3_2 import merge_sort_no_sentinels

# We use pytest's parametrize to run the same test logic on multiple input cases
@pytest.mark.parametrize("original", [
    [],                              # Empty list
    [1],                             # Single element
    [2, 1],                          # Two elements, unsorted
    [3, 2, 1],                       # Three elements, reverse order
    [5, 1, 4, 2, 8, 5, 2],           # List with duplicates
    [0, -1, -1, 3, 2, 2, 2, 1],      # List with negative numbers and duplicates
])
def test_merge_sort_no_sentinels_various_cases(original):
    """
    Test that merge_sort_no_sentinels correctly sorts various types of lists.
    """

    # Expected result is simply the Python built-in sorted() output
    expected = sorted(original)

    # Make a copy of the original list so we don't mutate the test data
    arr = list(original)

    # Call merge_sort_no_sentinels only if the list is not empty
    # For an empty list, p and r would both be 0, so we avoid negative indexing
    merge_sort_no_sentinels(arr, 0, len(arr) - 1 if arr else 0)

    # Check that the sorted array matches the expected sorted list
    assert arr == expected, f"For input {original}, expected {expected}, got {arr}"

    # Additional check: ensure the array is sorted in nondecreasing order
    assert all(arr[i] <= arr[i+1] for i in range(len(arr)-1)), \
        f"Result {arr} is not sorted in nondecreasing order."
