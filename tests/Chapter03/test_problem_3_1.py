import pytest
from src.Chapter03.Problem_3_1 import polynomial, degree, is_big_o, is_big_omega, is_big_theta

def test_case_a_k_greater_than_d():
    """
    Case (a): If k > d, then p(n) = O(n^k).
    Example: p(n) = 1 + 3n^2, d = 2, k = 3.
    """
    coeffs = [1, 0, 3]
    k = 3
    g = lambda n: n ** k
    p = lambda n: polynomial(n, coeffs)
    n_vals = range(50, 500, 50)
    assert is_big_o(p, g, n_vals, c=10)

def test_case_b_k_less_than_d():
    """
    Case (b): If k < d, then p(n) = Ω(n^k).
    Example: p(n) = 1 + 3n^2, d = 2, k = 1.
    """
    coeffs = [1, 0, 3]
    k = 1
    g = lambda n: n ** k
    p = lambda n: polynomial(n, coeffs)
    n_vals = range(50, 500, 50)
    assert is_big_omega(p, g, n_vals, c=0.1)

def test_case_c_k_equal_d():
    """
    Case (c): If k = d, then p(n) = Θ(n^k).
    Example: p(n) = 1 + 3n^2, d = 2, k = 2.
    """
    coeffs = [1, 0, 3]
    k = 2
    g = lambda n: n ** k
    p = lambda n: polynomial(n, coeffs)
    n_vals = range(50, 500, 50)
    assert is_big_theta(p, g, n_vals, c1=0.1, c2=10)

def test_case_d_k_greater_than_d_not_omega():
    """
    Case (d): If k > d, then p(n) != Ω(n^k).
    Example: p(n) = 1 + 3n^2, d = 2, k = 3.
    """
    coeffs = [1, 0, 3]
    k = 3
    g = lambda n: n ** k
    p = lambda n: polynomial(n, coeffs)
    n_vals = range(50, 500, 50)
    assert not is_big_omega(p, g, n_vals, c=0.1)

def test_case_e_k_less_than_d_not_big_o():
    """
    Case (e): If k < d, then p(n) != O(n^k).
    Example: p(n) = 1 + 3n^2, d = 2, k = 1.
    """
    coeffs = [1, 0, 3]
    k = 1
    g = lambda n: n ** k
    p = lambda n: polynomial(n, coeffs)
    n_vals = range(50, 500, 50)
    assert not is_big_o(p, g, n_vals, c=10)

def test_case_f_k_not_equal_d_not_theta():
    """
    Case (f): If k != d, then p(n) != Θ(n^k).
    Example: p(n) = 1 + 3n^2, d = 2, k = 1.
    """
    coeffs = [1, 0, 3]
    k = 1
    g = lambda n: n ** k
    p = lambda n: polynomial(n, coeffs)
    n_vals = range(50, 500, 50)
    assert not is_big_theta(p, g, n_vals, c1=0.1, c2=10)
