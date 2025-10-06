"""
Tests for Problem 5-1
English:
We check if expected value and variance estimation functions return correct results.
Polish:
Sprawdzamy, czy funkcje wartości oczekiwanej i wariancji zwracają poprawne wyniki.
"""

import pytest
from src.Chapter05.Problem_5_1 import expected_value_after_n_increments, variance_estimate

def test_expected_value():
    # Expected value should equal n
    assert expected_value_after_n_increments(5) == 5
    assert expected_value_after_n_increments(100) == 100

def test_variance_estimate():
    # Variance should scale linearly with n
    v1 = variance_estimate(1)
    v10 = variance_estimate(10)
    assert v10 > v1
    # Check proportionality
    assert abs(v10 / v1 - 10) < 1e-6
