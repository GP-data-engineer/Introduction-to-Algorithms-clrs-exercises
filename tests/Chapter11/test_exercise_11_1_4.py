# Exercise 11.1-4 — tests
# EN: Tests for big direct-address dictionary with O(1) init and operations.
# PL: Testy dużego słownika z adresowaniem bezpośrednim z inicjalizacją i operacjami w O(1).

import pytest
from src.Chapter11.Exercise_11_1_4 import BigDirectDict

def test_insert_and_search():
    d = BigDirectDict(50)
    d.insert(5, "k5", "v5")
    d.insert(25, "k25", "v25")
    assert d.search(5) == ("k5", "v5")
    assert d.search(25) == ("k25", "v25")
    assert d.search(10) is None

def test_delete_and_reuse_index():
    d = BigDirectDict(20)
    d.insert(3, "k3", "v3")
    d.insert(7, "k7", "v7")
    d.delete(3)
    assert d.search(3) is None
    d.insert(3, "k3b", "v3b")
    assert d.search(3) == ("k3b", "v3b")
