# Exercise 11.2-4 tests

import pytest
from src.Chapter11.Exercise_11_2_4 import FreeListHashTable


def test_allocate_free():
    ht = FreeListHashTable(3)
    idx = ht.allocate(10)
    assert ht.table[idx] == 10
    ht.free(idx)
    assert ht.table[idx] is None
