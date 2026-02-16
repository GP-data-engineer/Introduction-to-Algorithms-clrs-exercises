# Exercise 11.2-3 tests

import pytest
from src.Chapter11.Exercise_11_2_3 import SortedChainHashTable


def test_sorted_chain_insert_search():
    ht = SortedChainHashTable(5)
    ht.insert(10)
    ht.insert(5)
    assert ht.search(10)
    assert ht.search(5)


def test_sorted_chain_delete():
    ht = SortedChainHashTable(5)
    ht.insert(10)
    assert ht.delete(10)
    assert not ht.search(10)
