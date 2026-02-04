# EN: Tests for printing keys in left-child/right-sibling representation.
# PL: Testy wypisywania kluczy w reprezentacji „na lewo syn, na prawo brat”.

import pytest
from src.Chapter10.Exercise_10_4_4 import LCNode, print_lcrs_keys

def test_lcrs_preorder():
    c3 = LCNode(4)
    c2 = LCNode(3, right_sibling=c3)
    c1 = LCNode(2, right_sibling=c2)
    root = LCNode(1, left_child=c1)
    assert print_lcrs_keys(root) == [1, 2, 3, 4]

def test_lcrs_single_node():
    root = LCNode(10)
    assert print_lcrs_keys(root) == [10]
