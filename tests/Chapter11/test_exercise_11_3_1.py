import pytest
from src.Chapter11.Exercise_11_3_1 import HashedList


def test_search_found():
    hl = HashedList()
    h = hash("key")
    hl.insert("key", h)
    assert hl.search("key", h)


def test_search_not_found():
    hl = HashedList()
    hl.insert("key", hash("key"))
    assert not hl.search("other", hash("other"))
