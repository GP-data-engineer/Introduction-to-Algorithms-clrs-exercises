"""
Unit tests for Exercise 3.2.8.
Tests the numerical approximation of k from the equation k * ln(k) ≈ n
and verifies the asymptotic relationship k = Θ(n / ln(n)).
"""

import math
import pytest
from Exercise_3_2_8 import k_from_n, check_asymptotic_relation


def test_k_from_n_positive_values():
    # For large n, k should be close to n / ln(n)
    for n in [10, 100, 1000, 10_000]:
        k_val = k_from_n(n)
        approx = n / math.log(n)
        ratio = k_val / approx
        assert 0.9 <= ratio <= 1.1  # within 10%


def test_invalid_input():
    # n must be positive
    with pytest.raises(ValueError):
        k_from_n(0)
    with pytest.raises(ValueError):
        k_from_n(-5)


def test_asymptotic_relation():
    # The asymptotic check should pass for large n
    for n in [100, 1000, 10_000]:
        assert check_asymptotic_relation(n)
