import pytest
from src.Chapter03.Exercise_3_1_2 import is_theta_equivalent

def test_positive_a():
    # a > 0, b > 0
    assert is_theta_equivalent(5, 2, range(1, 1000))

def test_negative_a():
    # a < 0, b > 0
    assert is_theta_equivalent(-3, 3, range(10, 1000))  # start from n > |a|

def test_fractional_b():
    # fractional exponent b > 0
    assert is_theta_equivalent(2, 0.5, range(1, 1000))

def test_invalid_b():
    # b <= 0 should raise ValueError
    with pytest.raises(ValueError):
        is_theta_equivalent(1, 0, range(1, 100))
