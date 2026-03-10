import pytest
from src.Chapter12.Exercise_12_1_4 import Node, preorder, postorder

def test_preorder():
    root = Node(2, Node(1), Node(3))
    assert preorder(root) == [2, 1, 3]

def test_postorder():
    root = Node(2, Node(1), Node(3))
    assert postorder(root) == [1, 3, 2]
