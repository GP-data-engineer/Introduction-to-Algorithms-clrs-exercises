# EN: Tests for Morris inorder traversal with O(1) extra space.
# PL: Testy przejścia Morrisa (inorder) ze stałą pamięcią.

import pytest
from src.Chapter10.Exercise_10_4_5 import Node, morris_inorder_keys

def test_morris_inorder_simple():
    root = Node(2, Node(1), Node(3))
    assert morris_inorder_keys(root) == [1, 2, 3]

def test_morris_inorder_unbalanced():
    root = Node(1, None, Node(2, None, Node(3)))
    assert morris_inorder_keys(root) == [1, 2, 3]
