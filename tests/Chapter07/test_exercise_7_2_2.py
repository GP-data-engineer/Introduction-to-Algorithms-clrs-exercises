# test_exercise_7_2_2.py
# Tests for Exercise_7_2_2.py

import pytest
from src.Chapter06 import Exercise_7_2_2 as ex

def test_all_equal_quicksort_counts():
    # For n elements all equal, Lomuto partition will do comparisons ~ n(n-1)/2 (worst-case quadratic)
    for n in [10, 20, 40]:
        arr = [7] * n
        _, counters = ex.quicksort_count(arr)
        comparisons = counters['comparisons']
        # worst-case comparisons for classic quicksort ~ n(n-1)/2 but partition makes n-1 per top call etc.
        expected_upper = n * (n - 1) // 2 * 2  # loose upper bound
        assert comparisons >= n - 1  # at least linear
        assert comparisons <= expected_upper
