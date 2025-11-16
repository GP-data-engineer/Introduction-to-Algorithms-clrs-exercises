# Testy do zadania 9.1-1 — CLRS
# Tests for second smallest number algorithm

import pytest
from src.Chapter08.Exercise_9_1_1 import znajdz_druga_najmniejsza

def test_przyklad_podstawowy():
    assert znajdz_druga_najmniejsza([5, 3, 8, 2, 7, 1, 4]) == 2

def test_posortowane():
    assert znajdz_druga_najmniejsza([1, 2, 3, 4]) == 2

def test_odwrocone():
    assert znajdz_druga_najmniejsza([4, 3, 2, 1]) == 2

def test_duplikaty():
    assert znajdz_druga_najmniejsza([1, 1, 2, 2]) == 2

def test_blad_dla_jednego_elementu():
    with pytest.raises(ValueError):
        znajdz_druga_najmniejsza([42])
