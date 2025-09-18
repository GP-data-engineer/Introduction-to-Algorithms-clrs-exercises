# Unit tests for Exercise 4.3-1
# Verifies correctness of recurrence_4_3_1 implementation

import pytest
from src.Chapter04.Exercise_4_3_1 import recurrence_4_3_1

def test_recurrence_4_3_1_small():
    # Test base and small values
    assert recurrence_4_3_1(1) == 1
    assert recurrence_4_3_1(2) == 3
    assert recurrence_4_3_1(4) == 7

def test_recurrence_4_3_1_growth():
    # For n = 16, expected result is 31
    assert recurrence_4_3_1(16) == 31
