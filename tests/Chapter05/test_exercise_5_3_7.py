"""
Tests for Exercise 5.3-7
English: We check if RANDOM-SAMPLE returns a subset of correct size and range.
Polish: Sprawdzamy, czy RANDOM-SAMPLE zwraca podzbiór o poprawnym rozmiarze i zakresie.
"""

import pytest
from src.Chapter05.Exercise_5_3_7 import RANDOM_SAMPLE

def test_random_sample_size_and_range():
    result = RANDOM_SAMPLE(3, 10)
    assert len(result) == 3
    assert all(1 <= x <= 10 for x in result)
