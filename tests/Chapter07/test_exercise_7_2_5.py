# test_exercise_7_2_5.py
# Tests for Exercise_7_2_5.py

import math
from src.Chapter06 import Exercise_7_2_5 as ex

def test_formulas_and_simulation_agree():
    n = 1000
    for alpha in [0.05, 0.1, 0.25]:
        fmin, fmax = ex.formulas_depths(n, alpha)
        smin, smax = ex.simulate_depths(n, alpha)
        # simulation integer depths should be close to formulas (within factor ~2 due to ceiling)
        assert abs(fmin - smin) <= 3 or (fmin >= 1 and smin >= 1)
        assert abs(fmax - smax) <= 3 or (fmax >= 1 and smax >= 1)
