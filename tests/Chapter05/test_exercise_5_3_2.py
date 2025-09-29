"""
Tests for Exercise 5.3-2
English: We check if the answer is False.
Polish: Sprawdzamy, czy odpowiedź to False.
"""

import pytest
from src.Chapter05.Exercise_5_3_2 import permute_without_identity_valid

def test_permute_without_identity_valid():
    assert permute_without_identity_valid() is False
