"""
Tests for Exercise 4.5-4
We check if all methods return the correct asymptotic solution and largest r.
"""

import pytest
from src.Chapter04.Exercise_4_5_4 import (
    master_theorem, recursion_tree, substitution_method, largest_r
)

def test_master_theorem():
    assert "Θ(n^log₂3)" in master_theorem()

def test_recursion_tree():
    assert "Θ(n^log₂3)" in recursion_tree()

def test_substitution_method():
    assert "Θ(n^log₂3)" in substitution_method()

def test_largest_r():
    val = largest_r()
    assert 1.58 < val < 1.59
