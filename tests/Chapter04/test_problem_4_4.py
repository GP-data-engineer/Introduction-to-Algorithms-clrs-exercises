"""
Tests for Problem 4-4
We check generating function identities and Binet's formula.
"""

import pytest
from src.Chapter04.Problem_4_4 import (
    generating_function_identity, generating_function_closed,
    binet_formula, nearest_integer_property
)

def test_generating_function_identity():
    assert "F(z)" in generating_function_identity(0.5)

def test_generating_function_closed():
    assert generating_function_closed() == "(1 - z) / (1 - z - z^2)"

def test_binet_formula():
    # First Fibonacci numbers: 1, 1, 2, 3, 5, 8
    assert binet_formula(1) == 1
    assert binet_formula(2) == 1
    assert binet_formula(3) == 2
    assert binet_formula(6) == 8

def test_nearest_integer_property():
    # Should match Fibonacci sequence as well
    assert nearest_integer_property(1) == 1
    assert nearest_integer_property(2) == 1
    assert nearest_integer_property(3) == 2
    assert nearest_integer_property(7) == 13
