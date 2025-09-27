"""
Tests for Exercise 4.5-5
We check if the example returns the expected constants and function.
"""

import pytest
from src.Chapter04.Exercise_4_5_5 import example_case

def test_example_case():
    a, b, f = example_case()
    assert a == 2
    assert b == 2
    assert f == "n^2 / log n"
