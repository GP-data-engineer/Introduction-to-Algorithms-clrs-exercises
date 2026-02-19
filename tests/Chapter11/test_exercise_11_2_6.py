# Exercise 11.2-6 tests

import pytest
from src.Chapter11.Exercise_11_2_6 import RandomHashTable


def test_random_key_not_none():
    table = [[1], [], [2]]
    ht = RandomHashTable(table)
    assert ht.random_key() in [1, 2]


def test_random_key_empty():
    table = [[], [], []]
    ht = RandomHashTable(table)
    assert ht.random_key() is None
