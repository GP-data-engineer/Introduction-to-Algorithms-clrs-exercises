# test_exercise_7_2_3.py
# Tests for Exercise_7_2_3.py

import pytest
from src.Chapter06 import Exercise_7_2_3 as ex

def test_decreasing_array_quadratic_behavior():
    for n in [20, 50]:
        arr = list(range(n, 0, -1))
        _, counters = ex.quicksort_count(arr)
        comparisons = counters['comparisons']
        # For worst-case quicksort approximated comparisons ~ n(n-1)/2
        approx = n * (n - 1) // 2
        # Allow some leeway
        assert comparisons >= approx * 0.4
        assert comparisons <= approx * 2.0
