# Testy do zadania 9.1-2 — CLRS
# Tests for min-max algorithm

import pytest
from src.Chapter08.Exercise_9_1_2 import znajdz_min_max

def test_przyklad_podstawowy():
    assert znajdz_min_max([5, 3, 8, 2, 7, 1, 4]) == (1, 8)

def test_posortowane():
    assert znajdz_min_max([1, 2, 3, 4]) == (1, 4)

def test_odwrocone():
    assert znajdz_min_max([4, 3, 2, 1]) == (1, 4)

def test_jeden_element():
    assert znajdz_min_max([42]) == (42, 42)

def test_pusta_tablica():
    with pytest.raises(ValueError):
        znajdz_min_max([])
