"""
Tests for Exercise 4.5-3
We check if the solution matches Θ(n log log n).
"""

import pytest
from src.Chapter04.Exercise_4_5_3 import recurrence_solution

def test_recurrence_solution():
    assert recurrence_solution() == "Θ(n log log n)"
