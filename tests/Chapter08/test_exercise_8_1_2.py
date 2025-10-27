# test_exercise_8_1_2.py
import pytest
from src.Chapter06 import Exercise_8_1_2 as ex
import math

def test_direct_sum_agrees_with_lgamma():
    for n in [1, 2, 5, 10, 50]:
        exact_sum = ex.direct_sum_log2(n)
        # math.lgamma gives ln(n!), convert to log2
        ln_n_fact = math.lgamma(n + 1)
        lg2_via_lgamma = ln_n_fact / math.log(2.0)
        assert abs(exact_sum - lg2_via_lgamma) < 1e-9

def test_asymptotic_behavior_theta_n_log_n():
    # Check ratio lg(n!) / (n log2 n) approaches 1
    for n in [50, 200, 1000]:
        exact = ex.direct_sum_log2(n)
        ratio = exact / (n * math.log2(n))
        # ratio should be less than 1 but approach 1 as n grows (within tolerance)
        assert 0.8 < ratio < 1.02
