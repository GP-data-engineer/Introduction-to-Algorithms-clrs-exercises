"""
Tests for Exercise 4.6-3
We check if the explanation string matches the expected statement.
"""

import pytest
from src.Chapter04.Exercise_4_6_3 import regularity_implication

def test_regularity_implication():
    assert "Ω(n^(log_b a + ε))" in regularity_implication()
