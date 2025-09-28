"""
Tests for Exercise 5.2.5
English: We check if expected inversions formula is correct.
Polish: Sprawdzamy, czy wzór na oczekiwaną liczbę inwersji jest poprawny.
"""

import pytest
from src.Chapter05.Exercise_5_2_5 import expected_inversions

def test_expected_inversions():
    assert expected_inversions(5) == 5
    assert expected_inversions(4) == 3
