# Exercise 11.1-3 — tests
# EN: Tests for direct-address table with duplicate keys and O(1) delete by pointer.
# PL: Testy tablicy z adresowaniem bezpośrednim z powtarzającymi się kluczami i usuwaniem po wskaźniku.

import pytest
from src.Chapter11.Exercise_11_1_3 import DirectAddressMulti

def test_insert_and_search_multiple():
    d = DirectAddressMulti(10)
    n1 = d.insert(4, "x")
    n2 = d.insert(4, "y")
    head = d.search(4)
    assert head in (n1, n2)
    assert head.next in (n1, n2)
    assert head is not head.next

def test_delete_by_pointer():
    d = DirectAddressMulti(10)
    n1 = d.insert(5, "a")
    n2 = d.insert(5, "b")
    d.delete(n2)
    head = d.search(5)
    assert head is n1
    assert head.next is None
