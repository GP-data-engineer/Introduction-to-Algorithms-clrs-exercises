"""
Unit tests for Exercise 4.2-4 (theoretical computation of k threshold).
"""

import pytest
from src.Chapter04.Exercise_4_2_4 import compute_k_threshold


def test_compute_k_threshold_type():
    k = compute_k_threshold()
    assert isinstance(k, int)


def test_compute_k_threshold_value():
    k = compute_k_threshold()
    assert k > 0
