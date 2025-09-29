"""
Tests for Exercise 5.3-4
English: We check if the answer is False.
Polish: Sprawdzamy, czy odpowiedź to False.
"""

import pytest
from src.Chapter05.Exercise_5_3_4 import permute_by_cyclic_uniform

def test_permute_by_cyclic_uniform():
    assert permute_by_cyclic_uniform() is False
