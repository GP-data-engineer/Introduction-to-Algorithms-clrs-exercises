import pytest
from src.Chapter12.Exercise_12_2_1 import is_valid_bst_search


def test_valid():
    assert is_valid_bst_search([10, 5, 7], 7)


def test_invalid():
    assert not is_valid_bst_search([10, 5, 12, 6], 6)