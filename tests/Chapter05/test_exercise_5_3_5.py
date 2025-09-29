"""
Tests for Exercise 5.3-5
English: We check if probability formula is correct.
Polish: Sprawdzamy, czy wzór na prawdopodobieństwo jest poprawny.
"""

import pytest
from src.Chapter05.Exercise_5_5 import distinct_priorities_probability

def test_distinct_priorities_probability():
    assert abs(distinct_priorities_probability(10) - 0.9) < 1e-9
