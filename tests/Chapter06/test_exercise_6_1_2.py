"""
Tests for Exercise 6.1-2
"""

import pytest
from src.Chapter06.Exercise_6_1_2 import heap_height

def test_heap_height():
    assert heap_height(1) == 0
    assert heap_height(10) == 3
