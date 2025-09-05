import pytest
from src.Chapter03.Exercise_3_1_4 import is_big_o_of, expr1, bound1, expr2, bound2

def test_expr1_is_big_o_bound1():
    n_values = range(1, 100)
    assert is_big_o_of(lambda n: expr1(n, 7), bound1, n_values)

def test_expr2_is_big_o_bound2():
    n_values = range(1, 20)
    assert is_big_o_of(lambda n: expr2(n, 4), bound2, n_values)

def test_not_big_o_when_bound_too_small():
    # 2^n is NOT O(n^2)
    assert not is_big_o_of(lambda n: 2 ** n, lambda n: n ** 2, range(1, 20))
