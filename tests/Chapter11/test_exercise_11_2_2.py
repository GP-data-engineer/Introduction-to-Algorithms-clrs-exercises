# Exercise 11.2-2 tests

import pytest
from src.Chapter11.Exercise_11_2_2 import HashTableChaining


def test_hash_insert():
    ht = HashTableChaining(9)
    keys = [5, 28, 19]
    for k in keys:
        ht.insert(k)
    assert 5 in ht.get_table()[5]
    assert 28 in ht.get_table()[1]
    assert 19 in ht.get_table()[1]
