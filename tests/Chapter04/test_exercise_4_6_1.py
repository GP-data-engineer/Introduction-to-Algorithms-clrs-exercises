"""
Tests for Exercise 4.6-1
We check if n_j is computed correctly for integer b.
"""

import pytest
from src.Chapter04.Exercise_4_6_1 import n_j

def test_n_j():
    assert n_j(64, 2, 3) == 8
    assert n_j(81, 3, 2) == 9
