import pytest
from src.Chapter03.Exercise_3_1_1 import is_theta_equivalent

# ------------------- TESTS -------------------

def test_theta_equivalence_polynomial():
    # f(n) grows faster than g(n)
    def f(n): return n**2
    def g(n): return n
    n_values = range(1, 1000)
    assert is_theta_equivalent(f, g, n_values)

def test_theta_equivalence_equal_growth():
    # f(n) and g(n) grow at the same rate
    def f(n): return n
    def g(n): return 3 * n
    n_values = range(1, 1000)
    assert is_theta_equivalent(f, g, n_values)

def test_theta_equivalence_different_orders():
    # f(n) grows faster than g(n) but both are non-negative
    def f(n): return n**3
    def g(n): return n**2
    n_values = range(1, 1000)
    assert is_theta_equivalent(f, g, n_values)
