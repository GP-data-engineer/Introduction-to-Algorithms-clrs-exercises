import pytest
from src.Chapter12.Exercise_12_1_1 import bst_drawings_description

def test_description_exists():
    text = bst_drawings_description()
    assert isinstance(text, str)
    assert "BST" in text
