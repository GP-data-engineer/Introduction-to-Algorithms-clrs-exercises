import pytest
from src.Chapter11.Exercise_11_4_2 import HashTableOpen, DELETED

def test_insert_and_delete():
    h = HashTableOpen(11)
    h.insert(10)
    h.insert(21)
    h.delete(10)
    assert h.T[h.search(21)] == 21
    assert DELETED in h.T
