import pytest
from src.Chapter03.Exercise_3_1_7 import is_little_o, is_little_omega, intersection_nonempty

def test_slower_function():
    """
    Positive case for o(g):
    f(n) = sqrt(n) grows slower than g(n) = n.
    Expected: f ∈ o(g), f ∉ ω(g), intersection is False.
    """
    g = lambda n: n
    f = lambda n: n**0.5
    n_values = range(10, 10000, 100)
    assert is_little_o(f, g, n_values)
    assert not is_little_omega(f, g, n_values)
    assert not intersection_nonempty(f, g, n_values)

def test_faster_function():
    """
    Positive case for ω(g):
    f(n) = n^2 grows faster than g(n) = n.
    Expected: f ∉ o(g), f ∈ ω(g), intersection is False.
    """
    g = lambda n: n
    f = lambda n: n**2
    n_values = range(10, 10000, 100)
    assert not is_little_o(f, g, n_values)
    assert is_little_omega(f, g, n_values)
    assert not intersection_nonempty(f, g, n_values)

def test_same_growth_rate():
    """
    Neither o(g) nor ω(g):
    f(n) = 3n has the same growth rate as g(n) = n.
    Expected: f ∉ o(g), f ∉ ω(g), intersection is False.
    """
    g = lambda n: n
    f = lambda n: 3 * n
    n_values = range(10, 10000, 100)
    assert not is_little_o(f, g, n_values)
    assert not is_little_omega(f, g, n_values)
    assert not intersection_nonempty(f, g, n_values)

def test_no_function_in_both():
    """
    Theorem check:
    There should be no function that is both in o(g) and ω(g).
    """
    g = lambda n: n
    # Try a function that changes growth rate (artificial case)
    f = lambda n: n if n % 2 == 0 else n**2
    n_values = range(10, 10000, 100)
    assert not intersection_nonempty(f, g, n_values)
