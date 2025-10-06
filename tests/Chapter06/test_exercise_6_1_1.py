"""
Tests for Exercise 6.1-1
"""

import pytest
from src.Chapter06.Exercise_6_1_1 import heap_elements_range

def test_heap_elements_range():
    assert heap_elements_range(1) == (2, 3)
    assert heap_elements_range(3) == (8, 15)
