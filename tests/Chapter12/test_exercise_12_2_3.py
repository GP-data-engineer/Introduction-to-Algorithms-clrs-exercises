import pytest
from src.Chapter12.Exercise_12_2_3 import Node, tree_predecessor

def test_predecessor():
    a = Node(20)
    b = Node(10)
    c = Node(30)
    a.left = b
    a.right = c
    b.parent = a
    c.parent = a
    assert tree_predecessor(c).key == 20
