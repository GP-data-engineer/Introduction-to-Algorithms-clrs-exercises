"""
Unit tests for Exercise 4.2-7.
Tests multiplication of complex numbers using only 3 real multiplications.
"""

import pytest
from src.Chapter04.Exercise_4_2_7 import multiply_complex_3muls

def test_positive_numbers():
    # (3 + 2i) * (1 + 4i) = 3*1 - 2*4 + (3*4 + 2*1)i = -5 + 14i
    assert multiply_complex_3muls(3, 2, 1, 4) == (-5, 14)

def test_negative_numbers():
    # (-2 + 5i) * (4 - 3i) = (-8 - 15) + (-2*-3 + 5*4)i = -23 + 26i
    assert multiply_complex_3muls(-2, 5, 4, -3) == (7, 26)

def test_with_zero():
    # (0 + 0i) * (7 + 9i) = 0 + 0i
    assert multiply_complex_3muls(0, 0, 7, 9) == (0, 0)

def test_pure_real_and_pure_imaginary():
    # (5 + 0i) * (0 + 3i) = 0 + 15i
    assert multiply_complex_3muls(5, 0, 0, 3) == (0, 15)

def test_commutativity():
    # Multiplication should be commutative
    result1 = multiply_complex_3muls(3, 2, 1, 4)
    result2 = multiply_complex_3muls(1, 4, 3, 2)
    assert result1 == result2
