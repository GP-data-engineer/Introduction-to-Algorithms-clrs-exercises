# Test for Exercise 10.4-1 — CLRS
# EN: Test building the tree and preorder traversal.
# PL: Test budowy drzewa i przejścia preorder.

import pytest
from src.Chapter10.Exercise_10_4_1 import build_tree_from_table, preorder

def test_preorder_from_table():
    root = build_tree_from_table()
    keys = preorder(root)
    # Sprawdzamy, że korzeń i kilka kluczy są na miejscu
    assert keys[0] == 8
    assert 12 in keys
    assert 21 in keys
    assert len(keys) == 10
