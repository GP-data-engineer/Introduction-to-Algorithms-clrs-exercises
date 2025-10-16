# test_exercise_7_2_6.py
# Tests for Exercise_7_2_6.py

import math
import random
from src.Chapter06 import Exercise_7_2_6 as ex

def test_theoretical_vs_approx():
    n = 101
    for alpha in [0.01, 0.05, 0.1, 0.2]:
        theo = ex.theoretical_probability(n, alpha)
        approx = 1 - 2 * alpha
        # Because of discrete rounding, theoretical should be close to approx (difference <= 1/n)
        assert abs(theo - approx) <= 0.05 + 1.0/n

def test_simulation_close_to_theoretical():
    random.seed(42)
    n = 101
    alpha = 0.1
    sim = ex.simulate_probability(n, alpha, trials=5000)
    theo = ex.theoretical_probability(n, alpha)
    assert abs(sim - theo) < 0.05
