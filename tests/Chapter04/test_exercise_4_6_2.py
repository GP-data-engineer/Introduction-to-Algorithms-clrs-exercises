"""
Tests for Exercise 4.6-2
We check if the solution matches the expected form.
"""

import pytest
from src.Chapter04.Exercise_4_6_2 import recurrence_solution

def test_recurrence_solution():
    assert recurrence_solution(0) == "Θ(n^(log_b a) log^1 n)"
    assert recurrence_solution(2) == "Θ(n^(log_b a) log^3 n)"
