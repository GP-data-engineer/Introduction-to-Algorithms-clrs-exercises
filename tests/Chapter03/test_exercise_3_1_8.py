import pytest
from src.Chapter03.Exercise_3_1_8 import is_big_o_2d, is_big_omega_2d, is_big_theta_2d

def test_same_growth_rate():
    """
    Positive case for Θ(g):
    f(n, m) = 3 * n * m has the same growth rate as g(n, m) = n * m.
    Expected: f ∈ O(g), f ∈ Ω(g), f ∈ Θ(g).
    """
    g = lambda n, m: n * m
    f = lambda n, m: 3 * n * m
    n_vals = range(50, 200, 50)
    m_vals = range(50, 200, 50)
    assert is_big_o_2d(f, g, n_vals, m_vals, c=3.1)
    assert is_big_omega_2d(f, g, n_vals, m_vals, c=2.9)
    assert is_big_theta_2d(f, g, n_vals, m_vals, c1=2.9, c2=3.1)

def test_slower_function():
    """
    Positive case for O(g) only:
    f(n, m) = n * sqrt(m) grows slower than g(n, m) = n * m.
    Expected: f ∈ O(g), f ∉ Ω(g), f ∉ Θ(g).
    """
    g = lambda n, m: n * m
    f = lambda n, m: n * (m ** 0.5)
    n_vals = range(50, 200, 50)
    m_vals = range(50, 200, 50)
    assert is_big_o_2d(f, g, n_vals, m_vals, c=1.0)
    assert not is_big_omega_2d(f, g, n_vals, m_vals, c=1.0)
    assert not is_big_theta_2d(f, g, n_vals, m_vals, c1=1.0, c2=1.0)

def test_faster_function():
    """
    Positive case for Ω(g) only:
    f(n, m) = n^2 * m^2 grows faster than g(n, m) = n * m.
    Expected: f ∉ O(g), f ∈ Ω(g), f ∉ Θ(g).
    """
    g = lambda n, m: n * m
    f = lambda n, m: (n ** 2) * (m ** 2)
    n_vals = range(50, 200, 50)
    m_vals = range(50, 200, 50)
    assert not is_big_o_2d(f, g, n_vals, m_vals, c=1.0)
    assert is_big_omega_2d(f, g, n_vals, m_vals, c=1.0)
    assert not is_big_theta_2d(f, g, n_vals, m_vals, c1=1.0, c2=1.0)

def test_equal_functions():
    """
    Positive case for Θ(g):
    f(n, m) = g(n, m) exactly.
    Expected: f ∈ O(g), f ∈ Ω(g), f ∈ Θ(g).
    """
    g = lambda n, m: n * m
    f = lambda n, m: n * m
    n_vals = range(50, 200, 50)
    m_vals = range(50, 200, 50)
    assert is_big_o_2d(f, g, n_vals, m_vals, c=1.0)
    assert is_big_omega_2d(f, g, n_vals, m_vals, c=1.0)
    assert is_big_theta_2d(f, g, n_vals, m_vals, c1=1.0, c2=1.0)
