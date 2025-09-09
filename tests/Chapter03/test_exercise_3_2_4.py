import pytest
from src.Chapter03.Exercise_3_2_4 import is_polynomially_bounded_factorial_log

def test_polynomial_bound():
    assert is_polynomially_bounded_factorial_log(1024, floor=True)
    assert is_polynomially_bounded_factorial_log(1024, floor=False)
