# test_exercise_7_2_4.py
# Tests for Exercise_7_2_4.py

import pytest
import random
from src.Chapter06 import Exercise_7_2_4 as ex

def test_insertion_better_on_nearly_sorted():
    random.seed(1)
    n = 300
    k_swaps = 3  # very few swaps -> nearly sorted
    arr = ex.generate_nearly_sorted(n, k_swaps)
    _, ins_c = ex.insertion_sort_count(arr)
    _, qs_c = ex.quicksort_count(arr)
    # insertion comparisons should be much smaller than quicksort comparisons for nearly sorted
    assert ins_c['comparisons'] < qs_c['comparisons']
    # insertion shifts roughly equals number of inversions; for tiny k expect small shifts
    assert ins_c['shifts'] <= 1000
