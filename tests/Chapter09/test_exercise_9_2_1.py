# Test for Exercise 9.2-1 — CLRS
# EN: Test that RANDOMIZED-SELECT never recurses on an empty array.
# PL: Test sprawdzający, że RANDOMIZED-SELECT nigdy nie wywołuje rekurencji dla pustej tablicy.

import pytest
from src.Chapter08.Exercise_9_2_1 import randomized_select

def test_randomized_select_no_empty_recursion():
    # Testujemy na tablicy z 5 elementami
    dane = [10, 20, 30, 40, 50]
    for i in range(1, len(dane) + 1):
        wynik = randomized_select(dane.copy(), 0, len(dane) - 1, i)
        assert wynik in dane

def test_randomized_select_single_element():
    # Test na tablicy jednoelementowej
    dane = [42]
    wynik = randomized_select(dane, 0, 0, 1)
    assert wynik == 42
