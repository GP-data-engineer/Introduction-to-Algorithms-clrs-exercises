"""
Tests for Exercise 5.2.2
English: We check if probability of hiring exactly two people is correct.
Polish: Sprawdzamy, czy prawdopodobieństwo zatrudnienia dokładnie dwóch osób jest poprawne.
"""

import pytest
from src.Chapter05.Exercise_5_2_2 import hire_two_probability

def test_hire_two_probability():
    assert abs(hire_two_probability(5) - 0.2) < 1e-9
