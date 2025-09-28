"""
Tests for Exercise 5.2.3
English: We check if expected hires equals harmonic number.
Polish: Sprawdzamy, czy oczekiwana liczba zatrudnionych odpowiada liczbie harmonicznej.
"""

import pytest
from src.Chapter05.Exercise_5_2_3 import expected_hires

def test_expected_hires():
    assert abs(expected_hires(5) - (1+0.5+0.333333+0.25+0.2)) < 1e-6
