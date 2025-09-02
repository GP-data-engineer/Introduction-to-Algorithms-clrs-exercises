"""
Tests for Problem 2.3 — Horner's Scheme

These tests verify that horner_evaluate correctly computes
the value of a polynomial for various inputs.
"""

import pytest
from src.Chapter02.Problem_2_3 import horner_evaluate

@pytest.mark.parametrize("coeffs, x, expected", [
    ([0], 5, 0),                          # Zero polynomial
    ([5], 10, 5),                         # Constant polynomial
    ([1, 1], 1, 2),                       # 1 + 1*x at x=1
    ([2, -6, 2, -1], 3, 2 - 6*3 + 2*9 - 27),  # Cubic polynomial
    ([1, 0, 0, 0], 2, 1),                 # Only constant term non-zero
    ([1, 2, 3], 0, 1),                    # x=0 returns a0
    ([1, 2, 3], 1, 6),                    # Sum of coefficients
    ([1, 2, 3], 2, 1 + 4 + 12),           # 1 + 2*2 + 3*4
])
def test_horner_evaluate(coeffs, x, expected):
    """
    Test that horner_evaluate returns the correct polynomial value.
    """
    result = horner_evaluate(coeffs, x)
    assert result == pytest.approx(expected), \
        f"For coefficients={coeffs} and x={x}, expected {expected}, got {result}"
