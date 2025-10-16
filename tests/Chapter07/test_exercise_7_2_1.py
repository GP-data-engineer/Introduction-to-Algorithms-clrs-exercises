# test_exercise_7_2_1.py
# Tests for Exercise_7_2_1.py
# Imports from src.Chapter06 as requested.

import math
import pytest
from src.Chapter06 import Exercise_7_2_1 as ex

def test_compute_recurrence_small():
    # With a=1,b=0,c=1 we can compute closed form: T(n)=1 + sum_{k=2..n} k = 1 + (n(n+1)/2 -1) = n(n+1)/2
    n = 10
    Tn = ex.compute_recurrence(n, c=1.0, a=1.0, b=0.0)
    expected = n * (n + 1) / 2
    assert Tn == pytest.approx(expected)

def test_theta_n_squared_growth():
    # Ratio T(n)/n^2 should approach 1/2 * a (with a=1 here => ~0.5) as n grows for a*n cost per level
    for n in [50, 200, 1000]:
        Tn, ratio = ex.compare_to_quadratic(n, c=1.0, a=1.0, b=0.0)
        assert 0.4 <= ratio <= 0.6  # rough bound around 0.5
