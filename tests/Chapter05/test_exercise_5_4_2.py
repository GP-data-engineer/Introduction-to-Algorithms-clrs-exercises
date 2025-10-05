"""
Tests for Exercise 5.4-2
English: We check if expected throws formula is correct.
Polish: Sprawdzamy, czy wzór na oczekiwaną liczbę rzutów jest poprawny.
"""

import pytest
from src.Chapter05.Exercise_5_4_2 import expected_throws_until_collision

def test_expected_throws_until_collision():
    val = expected_throws_until_collision(365)
    assert 20 < val < 30  # known range for birthday paradox
