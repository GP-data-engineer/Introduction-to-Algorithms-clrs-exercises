"""
Test for Exercise 2.3-1 (CLRS)

This test verifies that the `merge_sort_trace` function from
Exercise_2_3_1.py correctly implements merge sort and returns
a sorted list for the given input.

Expected behavior:
- Returns a new sorted list in nondecreasing order.
- Does not modify the original input list.
- Works correctly for the provided example array.
"""

import pytest
from src.Chapter02.Exercise_2_3_1 import merge_sort_trace

def test_merge_sort_trace_example_array(capsys):
    array = [3, 41, 52, 26, 38, 57, 9, 49]
    expected = sorted(array)
    original_copy = list(array)


    # Capture printed output (trace)
    result = merge_sort_trace(original_copy)
    captured = capsys.readouterr()

    # Check correctness of sorting
    assert result == expected, f"Expected {expected}, got {result}"

    # Ensure original list is unchanged
    assert original_copy == array, "The original list should not be modified."

    # Ensure trace output contains 'Splitting' and 'Merging' steps
    assert "Splitting:" in captured.out, "Trace output should contain 'Splitting:' lines."
    assert "Merging:" in captured.out, "Trace output should contain 'Merging:' lines."

    # Ensure result is sorted in nondecreasing order
    assert all(result[i] <= result[i+1] for i in range(len(result)-1)), \
        f"Result {result} is not sorted in nondecreasing order."












