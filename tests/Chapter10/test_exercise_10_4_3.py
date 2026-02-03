# EN: Tests for non-recursive stack-based key printing.
# PL: Testy nierekurencyjnego wypisywania kluczy z użyciem stosu.

import pytest
from src.Chapter10.Exercise_10_4_3 import Node, iterative_print_keys

def test_iterative_print_preorder():
    root = Node(1, Node(2, Node(4), Node(5)), Node(3))
    assert iterative_print_keys(root) == [1, 2, 4, 5, 3]

def test_iterative_print_empty():
    assert iterative_print_keys(None) == []
