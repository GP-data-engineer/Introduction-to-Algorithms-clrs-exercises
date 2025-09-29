"""
Tests for Exercise 5.3-3
English: We check if the answer is False.
Polish: Sprawdzamy, czy odpowiedź to False.
"""

import pytest
from src.Chapter05.Exercise_5_3_3 import permute_with_all_uniform

def test_permute_with_all_uniform():
    assert permute_with_all_uniform() is False
