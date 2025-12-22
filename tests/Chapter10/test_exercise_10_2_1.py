# Exercise 10.2-1 test (EN): Tests O(1) insert-after and delete-after operations on a singly linked list.
# Exercise 10.2-1 test (PL): Testuje operacje INSERT-AFTER i DELETE-AFTER w czasie O(1) na liście jednokierunkowej.

import pytest
from src.Chapter10.Exercise_10_2_1 import SinglyLinkedList, Node


def test_insert_head_and_after():
    lst = SinglyLinkedList()
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    lst.insert_head(n3)
    lst.insert_head(n2)
    lst.insert_head(n1)
    assert lst.to_list() == [1, 2, 3]
    n5 = Node(5)
    lst.insert_after(n2, n5)
    assert lst.to_list() == [1, 2, 5, 3]


def test_delete_after():
    lst = SinglyLinkedList()
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    lst.insert_head(n3)
    lst.insert_head(n2)
    lst.insert_head(n1)
    deleted = lst.delete_after(n1)
    assert deleted.key == 2
    assert lst.to_list() == [1, 3]
