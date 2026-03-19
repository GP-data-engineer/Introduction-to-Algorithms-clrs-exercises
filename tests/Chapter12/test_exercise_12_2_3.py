import pytest
from src.Chapter12.Exercise_12_2_3 import Node, tree_predecessor


def test_predecessor():
    root = Node(10)
    left = Node(5)
    root.left = left
    left.parent = root
    assert tree_predecessor(root).key == 5
