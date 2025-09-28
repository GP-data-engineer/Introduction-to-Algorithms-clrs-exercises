"""
Tests for Problem 4-1
We check if each recurrence solution matches the expected asymptotic bound.
"""

import pytest
from src.Chapter04.Problem_4_1 import (
    recurrence_a, recurrence_b, recurrence_c,
    recurrence_d, recurrence_e, recurrence_f, recurrence_g
)

def test_recurrence_a():
    assert recurrence_a() == "Θ(n^4)"

def test_recurrence_b():
    assert recurrence_b() == "Θ(n log n)"

def test_recurrence_c():
    assert recurrence_c() == "Θ(n^2 log n)"

def test_recurrence_d():
    assert recurrence_d() == "Θ(n^3)"

def test_recurrence_e():
    assert recurrence_e() == "Θ(√n log n)"

def test_recurrence_f():
    assert recurrence_f() == "Θ(n log n)"

def test_recurrence_g():
    assert recurrence_g() == "Θ(n^2)"
