# Exercise 11.1-2 — tests
# EN: Tests for bit-vector-based dynamic set representation.
# PL: Testy reprezentacji zbioru dynamicznego za pomocą wektora bitowego.

import pytest
from src.Chapter11.Exercise_11_1_2 import BitVectorSet

def test_bitvector_insert_search():
    s = BitVectorSet(10)
    s.insert(0)
    s.insert(9)
    assert s.search(0)
    assert s.search(9)
    assert not s.search(5)

def test_bitvector_delete():
    s = BitVectorSet(5)
    s.insert(2)
    assert s.search(2)
    s.delete(2)
    assert not s.search(2)
