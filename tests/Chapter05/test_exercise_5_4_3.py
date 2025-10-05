"""
Tests for Exercise 5.4-3
English: We check if the answer mentions mutual independence.
Polish: Sprawdzamy, czy odpowiedź wspomina o pełnej niezależności.
"""

import pytest
from src.Chapter05.Exercise_5_4_3 import independence_requirement

def test_independence_requirement():
    assert "Mutual independence" in independence_requirement()
