"""
Tests for Exercise 5.2.1
English: We check if probabilities are computed correctly.
Polish: Sprawdzamy, czy prawdopodobieństwa są poprawnie obliczone.
"""

import pytest
from src.Chapter05.Exercise_5_2_1 import hire_probabilities

def test_hire_probabilities():
    p1, p2 = hire_probabilities(5)
    assert abs(p1 - 0.2) < 1e-9
    assert abs(p2 - 0.2) < 1e-9
