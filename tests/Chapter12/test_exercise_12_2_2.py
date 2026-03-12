import pytest
from src.Chapter12.Exercise_12_2_2 import Node, tree_minimum, tree_maximum

def test_min_max():
    root = Node(20, Node(10), Node(30))
    assert tree_minimum(root).key == 10
    assert tree_maximum(root).key == 30
