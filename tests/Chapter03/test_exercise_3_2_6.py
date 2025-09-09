import pytest
from src.Chapter03.Exercise_3_2_6 import compare_factorial_growth

def test_factorial_growth():
    for n in range(3, 10):
        greater, smaller = compare_factorial_growth(n)
        assert greater
        assert smaller
