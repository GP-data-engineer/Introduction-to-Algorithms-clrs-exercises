"""
Tests for Exercise 4.5-2
We check if the computed maximum 'a' is correct.
"""

import pytest
from src.Chapter04.Exercise_4_5_2 import max_a

def test_max_a():
    assert max_a() == 5
