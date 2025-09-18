# Unit tests for Exercise 4.3-2
# Verifies correctness of recurrence_4_3_2 implementation

import pytest
from src.Chapter04.Exercise_4_3_2 import recurrence_4_3_2

def test_recurrence_4_3_2_small():
    # Test base and small values
    assert recurrence_4_3_2(1) == 1
    assert recurrence_4_3_2(2) == 2
    assert recurrence_4_3_2(4) == 3

def test_recurrence_4_3_2_log_growth():
    # For n = 16, expected result is 5
    assert recurrence_4_3_2(16) == 5
