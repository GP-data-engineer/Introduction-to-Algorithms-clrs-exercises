# Exercise 11.1-1 — tests
# EN: Tests for finding the maximum element in a direct-addressed set.
# PL: Testy wyszukiwania największego elementu w zbiorze z adresowaniem bezpośrednim.

import pytest
from src.Chapter11.Exercise_11_1_1 import DirectAddressSet

def test_max_element_basic():
    s = DirectAddressSet(10)
    s.insert(2)
    s.insert(5)
    s.insert(9)
    assert s.max_element() == 9

def test_max_element_after_deletes():
    s = DirectAddressSet(10)
    for k in [1, 4, 7]:
        s.insert(k)
    s.delete(7)
    assert s.max_element() == 4

def test_max_element_empty():
    s = DirectAddressSet(5)
    assert s.max_element() is None
