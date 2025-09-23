"""
Tests for Exercise 4.5-1
We check if the returned asymptotic results match the expected solutions.
"""

import pytest
from src.Chapter04.Exercise_4_5_1 import (
    recurrence_a, recurrence_b, recurrence_c, recurrence_d, recurrence_e
)

def test_recurrence_a():
    assert recurrence_a() == "Θ(n)"

def test_recurrence_b():
    assert recurrence_b() == "Θ(√n log n)"

def test_recurrence_c():
    assert recurrence_c() == "Θ(n²)"

def test_recurrence_d():
    assert recurrence_d() == "Θ(n² log n)"

def test_recurrence_e():
    assert recurrence_e() == "Θ(n³)"
