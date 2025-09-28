"""
Tests for Exercise 5.1.3
English: We check if FAIR_RANDOM returns only 0 or 1.
Polish: Sprawdzamy, czy FAIR_RANDOM zwraca tylko 0 lub 1.
"""

import pytest
from src.Chapter05.Exercise_5_1_3 import FAIR_RANDOM

def test_fair_random_values():
    for _ in range(50):
        val = FAIR_RANDOM(0.3)
        assert val in [0, 1]
