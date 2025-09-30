"""
Tests for Exercise 5.3-6
English: We check if permute_by_sorting returns a permutation of the input.
Polish: Sprawdzamy, czy permute_by_sorting zwraca permutację wejścia.
"""

import pytest
from src.Chapter05.Exercise_5_3_6 import permute_by_sorting

def test_permute_by_sorting():
    arr = [1, 2, 3, 4]
    result = permute_by_sorting(arr)
    assert sorted(result) == [1, 2, 3, 4]
