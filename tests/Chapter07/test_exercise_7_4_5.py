# test_exercise_7_4_5.py
# Tests for Exercise_7_4_5.py

from src.Chapter06 import Exercise_7_4_5 as ex
import random

def test_hybrid_estimate_and_behavior():
    random.seed(2)
    n = 300
    arr = list(range(n))
    random.shuffle(arr)
    for k in [5, 10, 30]:
        est = ex.hybrid_cost_estimate(n, k)
        sorted_arr, counters = ex.hybrid_sort(arr, k, seed=2)
        # final array must be sorted
        assert sorted_arr == sorted(arr)
        # estimates should be positive and increase with k*k term
        assert est > 0
        # insertion comparisons should not exceed n*k in typical cases; allow generous tolerance
        assert counters['ins_comparisons'] <= n * k * 2
