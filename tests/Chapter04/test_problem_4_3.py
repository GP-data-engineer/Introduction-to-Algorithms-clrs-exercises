"""
Tests for Problem 4-3
We check if each recurrence solution matches the expected asymptotic bound.
"""

import pytest
from src.Chapter04.Problem_4_3 import (
    recurrence_a, recurrence_b, recurrence_c, recurrence_d,
    recurrence_e, recurrence_f, recurrence_g, recurrence_h,
    recurrence_i, recurrence_j, recurrence_k, recurrence_l
)

def test_recurrence_a():
    assert "Θ(n^log_3 4)" in recurrence_a() or "Θ(n^1.26)" in recurrence_a()

def test_recurrence_b():
    assert recurrence_b() == "Θ(n^2)"

def test_recurrence_c():
    assert recurrence_c() == "Θ(n^2)"

def test_recurrence_d():
    assert recurrence_d() == "Θ(n^2)"

def test_recurrence_e():
    assert recurrence_e() == "Θ(n^2)"

def test_recurrence_f():
    assert recurrence_f() == "Θ(n^2)"

def test_recurrence_g():
    assert recurrence_g() == "Θ(n^2)"

def test_recurrence_h():
    assert recurrence_h() == "Θ(n)"

def test_recurrence_i():
    assert recurrence_i() == "Θ(n^2)"

def test_recurrence_j():
    assert recurrence_j() == "Θ(n^3)"

def test_recurrence_k():
    assert recurrence_k() == "Θ(n^2 log n)"

def test_recurrence_l():
    assert recurrence_l() == "Θ(n log log n)"
