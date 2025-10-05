"""
Tests for Exercise 5.4-7
English: We check if threshold formula is correct.
Polish: Sprawdzamy, czy wzór na próg jest poprawny.
"""

import pytest
from src.Chapter05.Exercise_5_4_7 import birthday_threshold
import math

def test_birthday_threshold():
    val = birthday_threshold(365)
    assert 20 < val < 30
