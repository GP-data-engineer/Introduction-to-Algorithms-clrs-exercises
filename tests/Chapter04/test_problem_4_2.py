"""
Tests for Problem 4-2
We check if the returned asymptotic costs match the expected results.
"""

import pytest
from src.Chapter04.Problem_4_2 import binary_search_cost, merge_sort_cost

def test_binary_search_cost():
    costs = binary_search_cost(16)
    assert costs["pointer"] == "Θ(log n)"
    assert costs["copy_full"] == "Θ(n)"
    assert costs["copy_subarray"] == "Θ(n)"

def test_merge_sort_cost():
    costs = merge_sort_cost(16)
    assert costs["pointer"] == "Θ(n log n)"
    assert costs["copy_full"] == "Θ(n log^2 n)"
    assert costs["copy_subarray"] == "Θ(n log n)"
