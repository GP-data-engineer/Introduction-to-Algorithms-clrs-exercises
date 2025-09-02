"""
Tests for Problem 2.4 — Counting Inversions

These tests verify that count_inversions correctly counts
the number of inversions in various arrays.
"""

import pytest
from src.Chapter02.Problem_2_4 import count_inversions

@pytest.mark.parametrize("arr, expected", [
    ([2, 3, 8, 6, 1], 5),      # Example from the problem statement
    ([1, 2, 3, 4, 5], 0),      # Already sorted
    ([5, 4, 3, 2, 1], 10),     # Reverse sorted: n*(n-1)/2 inversions
    ([1], 0),                  # Single element
    ([1, 3, 2], 1),            # One inversion (3, 2)
    ([4, 1, 3, 2], 4),         # Mixed order
])
def test_count_inversions(arr, expected):
    """
    Test that count_inversions returns the correct inversion count.
    """
    result = count_inversions(arr)
    assert result == expected, f"For array {arr}, expected {expected}, got {result}"
