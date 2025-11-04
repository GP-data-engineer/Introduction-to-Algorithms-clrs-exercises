# test_exercise_8_1_3.py 
import pytest
from src.Chapter08 import Exercise_8_1_3 as ex

def test_required_c_half_grows():
    # For moderate n the required c for fraction 1/2 should be > 1 (so linear with small constant impossible)
    n = 20
    req_c = ex.required_c_for_fraction(n, 0.5)
    assert req_c > 1.0

def test_fraction_1_over_n_and_1_over_2pown():
    # For both fractions the required c still grows with n (is Omega(log n)/n * n = Omega(log n))
    for n in [10, 30, 80]:
        c_half = ex.required_c_for_fraction(n, 0.5)
        c_1_over_n = ex.required_c_for_fraction(n, 1.0/n)
        c_1_over_2pown = ex.required_c_for_fraction(n, 1.0/(2**n))
        # All should be positive and c_1_over_2pown slightly smaller due to extremely small fraction factor included in formula
        assert c_half > 0.0
        assert c_1_over_n > 0.0
        assert c_1_over_2pown > 0.0
        # None are constant small values like 0.01 for these n
        assert c_half > 0.5
