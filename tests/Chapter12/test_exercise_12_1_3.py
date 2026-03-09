import pytest
from src.Chapter12.Exercise_12_1_3 import Node, inorder_nonrecursive

def test_inorder_basic():
    root = Node(2, Node(1), Node(3))
    assert inorder_nonrecursive(root) == [1, 2, 3]
