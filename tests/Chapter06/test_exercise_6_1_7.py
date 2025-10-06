"""
Tests for Exercise 6.1-7
"""

import pytest
from src.Chapter06.Exercise_6_1_7 import leaf_indices

def test_leaf_indices():
    assert leaf_indices(10) == [6, 7, 8, 9, 10]
    assert leaf_indices(7) == [4, 5, 6, 7]
