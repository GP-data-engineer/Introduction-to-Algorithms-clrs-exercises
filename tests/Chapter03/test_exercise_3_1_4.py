import pytest
from src.Chapter03.Exercise_3_1_4 import is_big_o_of, expr1, bound1, expr2, bound2

def test_expr1_is_big_o_bound1():
    """
    Positive case:
    C*2^(n+1) should be O(2^n) because it differs only by a constant factor.
    """
    n_values = range(1, 100)
    assert is_big_o_of(lambda n: expr1(n, 7), bound1, n_values)

def test_expr2_is_big_o_bound2():
    """
    Positive case:
    C*2^n should be O(2^(2^n)) because the bound grows much faster.
    """
    n_values = range(1, 20)
    assert is_big_o_of(lambda n: expr2(n, 4), bound2, n_values)

def test_not_big_o_when_bound_too_small():
    """
    Negative case:
    2^n is NOT O(n^2) because it grows faster than any polynomial.
    """
    assert not is_big_o_of(lambda n: 2 ** n, lambda n: n ** 2, range(1, 50))

def test_big_o_with_constant_factor():
    """
    Positive case:
    5*n^3 is O(n^3) because the growth rate is identical up to a constant.
    """
    assert is_big_o_of(lambda n: 5 * n**3, lambda n: n**3, range(1, 1000))

def test_not_big_o_for_faster_growth():
    """
    Negative case:
    n! is not O(2^n) because factorial grows faster than exponential.
    """
    from math import factorial
    assert not is_big_o_of(lambda n: factorial(n), lambda n: 2**n, range(1, 15))
