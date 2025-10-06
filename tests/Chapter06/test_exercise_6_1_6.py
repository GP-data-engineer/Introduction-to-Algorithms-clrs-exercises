"""
Tests for Exercise 6.1-6
"""

import pytest
from src.Chapter06.Exercise_6_1_6 import is_max_heap

def test_is_max_heap():
    seq = [23, 17, 14, 6, 13, 10, 1, 5, 7, 12]
    assert is_max_heap(seq) is True
    not_heap = [10, 20, 5]
    assert is_max_heap(not_heap) is False
