import pytest 
from src.Chapter07.Exercise_7_2_1 import recurrence_solution

def test_recurrence_solution():
    assert "Θ(n^2)" in recurrence_solution()
