"""
Test for Exercise 2.2-2 (CLRS)

This test verifies that the `merge_sort_no_sentinels` function from
Exercise_2_2_2.py correctly implements merge sort without using sentinels.

Expected behavior:
- Returns a new sorted list in nondecreasing order.
- Does not modify the original input list.
- Works correctly for empty lists, single-element lists, lists with duplicates,
  and lists containing negative numbers.
"""

import pytest
from src.Chapter02.Exercise_2_2_2 import merge_sort_no_sentinels
# Test cases: (input, expected sorted output)
@pytest.mark.parametrize("original", [
    [],
    [1],
    [2, 1],
    [3, 2, 1],
    [5, 1, 4, 2, 8, 5, 2],
    [0, -1, -1, 3, 2, 2, 2, 1],
])
def test_merge_sort_no_sentinels_various_cases(original):
    expected = sorted(original)
    # Copy to ensure original is not modified
    original_copy = list(original)

    result = merge_sort_no_sentinels(original_copy)
    # Check correctness
    assert result == expected, f"For input {original}, expected {expected}, got {result}"
    # Ensure original list is unchanged
    assert original_copy == original, "The original list should not be modified."
    # Ensure result is sorted in nondecreasing order
    assert all(result[i] <= result[i+1] for i in range(len(result)-1)), \
        f"Result {result} is not sorted in nondecreasing order."
