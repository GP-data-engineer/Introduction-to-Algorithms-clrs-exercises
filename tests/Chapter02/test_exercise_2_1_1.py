"""
Test for Exercise 2.1-1 (CLRS)

This test verifies that the `solve` function from Exercise_2_1_1.py
correctly implements the insertion sort algorithm for the given array:
A = [31, 41, 59, 26, 41, 58]

Expected behavior:
- The returned list should be sorted in non-decreasing order.
- The output should match the expected sorted list.
"""

import importlib
import types

def test_insertion_sort_fixed_array():
    # Dynamically import the exercise module
    exercise_module = importlib.import_module("src.Chapter02.Exercise_2_1_1")

    # Ensure the module has a callable 'solve' function
    assert hasattr(exercise_module, "solve"), "The module must define a 'solve' function."
    assert isinstance(exercise_module.solve, types.FunctionType), "'solve' must be a function."

    # Call the solve function
    result = exercise_module.solve()

    # Expected sorted array
    expected = sorted([31, 41, 59, 26, 41, 58])

    # Check if the result matches the expected sorted list
    assert result == expected, f"Expected {expected}, but got {result}"

    # Additional check: ensure the list is sorted in non-decreasing order
    assert all(result[i] <= result[i+1] for i in range(len(result)-1)), "The list is not sorted."
