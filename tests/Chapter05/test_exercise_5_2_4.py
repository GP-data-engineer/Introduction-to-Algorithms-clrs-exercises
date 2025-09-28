"""
Tests for Exercise 5.2.4
English: We check if expected number of fixed points is always 1.
Polish: Sprawdzamy, czy oczekiwana liczba trafień własnych kapeluszy to zawsze 1.
"""

import pytest
from src.Chapter05.Exercise_5_2_4 import expected_fixed_points

def test_expected_fixed_points():
    assert expected_fixed_points(10) == 1
    assert expected_fixed_points(100) == 1
