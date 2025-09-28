"""
Tests for Exercise 5.1.1
English: We check if linear_order produces a sorted list.
Polish: Sprawdzamy, czy linear_order zwraca posortowaną listę.
"""

import pytest
from src.Chapter05.Exercise_5_1_1 import linear_order

def test_linear_order():
    candidates = [5, 2, 4, 1, 3]
    result = linear_order(candidates, lambda a, b: a < b)
    assert result == sorted(candidates)
