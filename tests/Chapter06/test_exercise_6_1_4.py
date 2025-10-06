"""
Tests for Exercise 6.1-4
"""

import pytest
from src.Chapter06.Exercise_6_1_4 import min_in_max_heap_location

def test_min_in_max_heap_location():
    assert min_in_max_heap_location() == "Leaves"
