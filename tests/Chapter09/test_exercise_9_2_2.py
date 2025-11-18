# Test for Exercise 9.2-2 — CLRS
# EN: Test independence of indicator variable X and T(max(k - 1, n - k))
# PL: Test niezależności zmiennej wskaźnikowej X i T(max(k - 1, n - k))

import pytest
from src.Chapter08.Exercise_9_2_2 import simulate_independence

def test_independence_simulation_consistency():
    dane = [10, 20, 30, 40, 50, 60, 70]
    i = 4
    wynik = simulate_independence(dane, i)
    assert "X" in wynik
    assert "T(max(k-1, n-k))" in wynik
    assert wynik["wynik"] in dane
    assert isinstance(wynik["T(max(k-1, n-k))"], int)
