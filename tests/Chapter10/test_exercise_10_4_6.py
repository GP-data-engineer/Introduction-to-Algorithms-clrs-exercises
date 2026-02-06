# EN: Tests for compact parent/children access with two pointers and one boolean.
# PL: Testy kompaktowego dostępu do ojca i synów z dwoma wskaźnikami i jedną zmienną bool.

import pytest
from src.Chapter10.Exercise_10_4_6 import CompactNode, add_children, get_parent, get_children

def test_parent_access_constant_time():
    root = CompactNode(10)
    c1 = CompactNode(20)
    c2 = CompactNode(30)
    add_children(root, [c1, c2])
    assert get_parent(c1) is root
    assert get_parent(c2) is root

def test_children_access_proportional_to_count():
    root = CompactNode(1)
    children = [CompactNode(i) for i in range(2, 5)]
    add_children(root, children)
    result_keys = [c.key for c in get_children(root)]
    assert result_keys == [2, 3, 4]
