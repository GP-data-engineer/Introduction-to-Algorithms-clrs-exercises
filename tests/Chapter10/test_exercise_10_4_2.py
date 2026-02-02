# EN: Tests for recursive key printing in a binary tree.
# PL: Testy rekurencyjnego wypisywania kluczy drzewa binarnego.

import pytest
from src.Chapter10.Exercise_10_4_2 import Node, recursive_print_keys

def test_recursive_print_simple_tree():
    root = Node(1, Node(2), Node(3))
    assert recursive_print_keys(root) == [1, 2, 3]

def test_recursive_print_single_node():
    root = Node(42)
    assert recursive_print_keys(root) == [42]
