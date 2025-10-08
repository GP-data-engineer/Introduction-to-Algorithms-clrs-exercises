import pytest
from src.Chapter06.Exercise_6_3_3 import nodes_at_height

def test_nodes_at_height():
    assert nodes_at_height(16, 1) == 8
    assert nodes_at_height(16, 2) == 4
