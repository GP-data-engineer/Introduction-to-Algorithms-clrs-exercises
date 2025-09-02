"""
Test for Exercise 2.3-5 (CLRS)

This test verifies that the `binary_search` function from
Exercise_2_3_5.py correctly implements iterative binary search.

Expected behavior:
- Returns the correct index of the target if found.
- Returns -1 if the target is not present in the list.
- Works for empty lists, single-element lists, and lists with negative numbers.
"""

import pytest
from src.Chapter02.Exercise_2_3_5 import binary_search

@pytest.mark.parametrize("arr,target,expected_index", [
    ([], 5, -1),                          # Empty list
    ([1], 1, 0),                          # Single element, found
    ([1], 2, -1),                         # Single element, not found
    ([1, 3, 5, 7, 9], 1, 0),              # First element
    ([1, 3, 5, 7, 9], 9, 4),              # Last element
    ([1, 3, 5, 7, 9], 5, 2),              # Middle element
    ([1, 3, 5, 7, 9], 4, -1),             # Not found, between elements
    ([-5, -3, -1, 0, 2, 4], -3, 1),       # Negative number, found
    ([-5, -3, -1, 0, 2, 4], 3, -1),       # Negative number, not found
])
def test_binary_search_various_cases(arr, target, expected_index):
    """
    Test that binary_search returns the correct index for various cases.
    """

    result = binary_search(arr, target)

    # Check that the returned index matches the expected index
    assert result == expected_index, \
        f"For array {arr} and target {target}, expected index {expected_index}, got {result}"

    # If the target is found, verify that the element at the returned index is indeed the target
    if result != -1:
        assert arr[result] == target, \
            f"Returned index {result} does not match target {target} in array {arr}"
