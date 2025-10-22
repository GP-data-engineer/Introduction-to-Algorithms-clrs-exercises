# test_exercise_7_4_4.py
# Tests for Exercise_7_4_4.py

from src.Chapter06 import Exercise_7_4_4 as ex
import math

def test_expected_comparisons_grows_like_nlogn():
    ns = [8, 16, 32, 64]
    ratios = []
    for n in ns:
        e = ex.expected_comparisons_exact(n)
        ratios.append(e / (n * math.log2(n)))
    # ratios should be positive and roughly stable (Θ(n log n))
    assert all(r > 0 for r in ratios)
    assert ratios[-1] / ratios[0] < 5  # not exploding
