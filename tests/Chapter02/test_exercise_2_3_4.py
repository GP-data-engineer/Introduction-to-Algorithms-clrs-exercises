"""
Test for Exercise 2.3-4 (CLRS)

This test verifies that the `recursive_insertion_sort` function from
Exercise_2_3_4.py correctly implements recursive insertion sort and
returns both the sorted list and the number of comparisons made.

Expected behavior:
- Sorts the list in nondecreasing order in place.
- Returns a comparison count consistent with the algorithm's logic.
"""

import pytest
from src.Chapter02.Exercise_2_3_4 import recursive_insertion_sort

# We use pytest's parametrize to run the same test logic on multiple input cases
@pytest.mark.parametrize("original", [
    [],                              # Empty list
    [1],                             # Single element
    [2, 1],                          # Two elements, unsorted
    [3, 2, 1],                       # Three elements, reverse order
    [5, 1, 4, 2, 8, 5, 2],           # List with duplicates
    [0, -1, -1, 3, 2, 2, 2, 1],      # List with negative numbers and duplicates
])
def test_recursive_insertion_sort_various_cases(original):
    """
    Test that recursive_insertion_sort correctly sorts various types of lists
    and returns a valid comparison count.
    """

    # Expected result is simply the Python built-in sorted() output
    expected_sorted = sorted(original)

    # Make a copy of the original list so we don't mutate the test data
    arr_copy = list(original)

    # Call recursive_insertion_sort
    sorted_arr, comparisons = recursive_insertion_sort(arr_copy, len(arr_copy))

    # Check that the sorted array matches the expected sorted list
    assert sorted_arr == expected_sorted, \
        f"For input {original}, expected {expected_sorted}, got {sorted_arr}"

    # Additional check: ensure the array is sorted in nondecreasing order
    assert all(sorted_arr[i] <= sorted_arr[i+1] for i in range(len(sorted_arr)-1)), \
        f"Result {sorted_arr} is not sorted in nondecreasing order."

    # Check that comparisons is a non-negative integer
    assert isinstance(comparisons, int) and comparisons >= 0, \
        f"Comparisons count should be a non-negative integer, got {comparisons}"
