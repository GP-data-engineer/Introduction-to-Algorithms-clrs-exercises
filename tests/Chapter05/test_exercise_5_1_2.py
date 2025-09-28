"""
Tests for Exercise 5.1.2
English: We check if RANDOM(a, b) always returns values in the correct range.
Polish: Sprawdzamy, czy RANDOM(a, b) zawsze zwraca wartości w poprawnym zakresie.
"""

import pytest
from src.Chapter05.Exercise_5_1_2 import RANDOM

def test_random_range():
    for _ in range(100):
        val = RANDOM(5, 10)
        assert 5 <= val <= 10
