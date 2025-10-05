"""
Tests for Exercise 5.4-6
English: We check if expected values are within reasonable ranges.
Polish: Sprawdzamy, czy oczekiwane wartości są w rozsądnych zakresach.
"""

import pytest
from src.Chapter05.Exercise_5_4_6 import expected_bins

def test_expected_bins():
    empty, one, two = expected_bins(100)
    assert empty > 30 and empty < 40
    assert one > 30 and one < 40
    assert two > 15 and two < 25
