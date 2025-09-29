"""
Tests for Exercise 5.3-1
English: We check if randomize_in_place produces a permutation of the input.
Polish: Sprawdzamy, czy randomize_in_place zwraca permutację wejścia.
"""

import pytest
from src.Chapter05.Exercise_5_3_1 import randomize_in_place

def test_randomize_in_place():
    arr = [1, 2, 3, 4]
    result = randomize_in_place(arr[:])
    assert sorted(result) == [1, 2, 3, 4]
