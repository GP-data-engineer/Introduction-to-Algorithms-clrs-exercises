import pytest
from src.Chapter03.Exercise_3_1_5 import is_big_o, is_big_omega, is_big_theta

def test_polynomial_functions():
    f = lambda n: 4 * n**2 + 10
    g = lambda n: n**2
    n_values = range(10, 1000)
    assert is_big_o(f, g, n_values)
    assert is_big_omega(f, g, n_values)
    assert is_big_theta(f, g, n_values)

def test_different_growth_rates():
    f = lambda n: n
    g = lambda n: n**2
    n_values = range(10, 1000)
    assert is_big_o(f, g, n_values)
    assert not is_big_omega(f, g, n_values)
    assert not is_big_theta(f, g, n_values)

def test_exponential_vs_polynomial():
    f = lambda n: 2**n
    g = lambda n: n**5
    n_values = range(5, 30)
    assert not is_big_o(f, g, n_values)
    assert is_big_omega(f, g, n_values)
    assert not is_big_theta(f, g, n_values)

def test_equal_functions():
    f = lambda n: n**3
    g = lambda n: n**3
    n_values = range(1, 500)
    assert is_big_o(f, g, n_values)
    assert is_big_omega(f, g, n_values)
    assert is_big_theta(f, g, n_values)

def test_not_big_omega_for_slower_growth():
    f = lambda n: n**2
    g = lambda n: n**3
    n_values = range(10, 1000)
    assert is_big_o(f, g, n_values)
    assert not is_big_omega(f, g, n_values)
