# Test for Exercise 10.2-8 — CLRS
# EN: Test XOR-based doubly linked list operations.
# PL: Test operacji na liście dwukierunkowej z XOR.

import pytest
from src.Chapter10.Exercise_10_2_8 import XORLinkedList

def test_insert_and_traverse():
    l = XORLinkedList()
    l.insert(1)
    l.insert(2)
    l.insert(3)
    assert l.traverse() == [1, 2, 3]

def test_search():
    l = XORLinkedList()
    l.insert(5)
    l.insert(6)
    assert l.search(6).key == 6
    assert l.search(99) is None

def test_delete():
    l = XORLinkedList()
    l.insert(7)
    l.insert(8)
    l.insert(9)
    assert l.delete(8) is True
    assert l.traverse() == [7, 9]

def test_reverse():
    l = XORLinkedList()
    for x in [1, 2, 3]:
        l.insert(x)
    l.reverse()
    assert l.traverse() == [3, 2, 1]
