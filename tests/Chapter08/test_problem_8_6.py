"""
Testy do Problem 8.6 (PL): Sprawdzamy poprawność scalania i analizę dolnej granicy.
Tests for Problem 8.6 (EN): Verifies correctness of merging and lower bound analysis.
"""

import pytest
from src.Chapter08.Problem_8_6 import merge_sorted_lists, theoretical_lower_bound

def test_merge_correctness():
    A = [1, 3, 5]
    B = [2, 4, 6]
    merged, _ = merge_sorted_lists(A, B)
    assert merged == [1, 2, 3, 4, 5, 6]

def test_comparison_count():
    A = [1, 3, 5]
    B = [2, 4, 6]
    _, comparisons = merge_sorted_lists(A, B)
    assert comparisons == 5  # n = 3 → max comparisons = 2n - 1 = 5

def test_lower_bound_estimation():
    n = 4
    bound = theoretical_lower_bound(n)
    assert round(bound, 2) == round(log2(70), 2)  # comb(8,4) = 70
