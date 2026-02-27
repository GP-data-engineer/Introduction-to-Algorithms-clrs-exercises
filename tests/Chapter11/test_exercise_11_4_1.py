import pytest
from src.Chapter11.Exercise_11_4_1 import OpenAddressingHash

def test_linear_insert():
    h = OpenAddressingHash(11)
    h.insert(10, "linear")
    assert h.T[10] == 10

def test_quadratic_insert():
    h = OpenAddressingHash(11)
    h.insert(10, "quadratic")
    assert h.T[10] == 10

def test_double_insert():
    h = OpenAddressingHash(11)
    h.insert(10, "double")
    assert h.T[10] == 10
