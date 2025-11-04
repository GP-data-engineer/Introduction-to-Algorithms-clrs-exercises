# test_exercise_7_4_2.py
# Tests for Exercise_7_4_2.py

from src.Chapter07 import Exercise_7_4_2 as ex
import math

def test_balanced_quicksort_comparisons_scale_like_nlogn():
    ns = [32, 128, 512]
    ratios = []
    for n in ns:
        _, counters = ex.balanced_quicksort_count(list(range(n)))
        comps = counters['comparisons']
        ratios.append(comps / (n * math.log2(n)))
    # ratios should be within same order of magnitude
    assert ratios[0] > 0
    assert 0.1 < ratios[1] / ratios[0] < 10
    assert 0.1 < ratios[2] / ratios[1] < 10
