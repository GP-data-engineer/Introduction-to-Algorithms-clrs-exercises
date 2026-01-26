import pytest
from src.Chapter10.Exercise_10_2_4 import LinkedList

def test_search_found():
    l = LinkedList()
    l.insert(1)
    l.insert(2)
    l.insert(3)
    assert l.search(2).key == 2

def test_search_not_found():
    l = LinkedList()
    l.insert(5)
    l.insert(6)
    assert l.search(99) is None
