import pytest
from src.Chapter12.Exercise_12_2_2 import Node, tree_minimum, tree_maximum


def test_min_max():
    root = Node(10)
    root.left = Node(5)
    root.right = Node(20)
    assert tree_minimum(root).key == 5
    assert tree_maximum(root).key == 20