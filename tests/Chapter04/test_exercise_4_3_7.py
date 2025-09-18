# Unit tests for Exercise 4.3-7
# Verifies correctness of recurrence_4_3_7 implementation

import pytest
from src.Chapter04.Exercise_4_3_7 import recurrence_4_3_7

@pytest.mark.parametrize("n,expected", [
    (1, 1),
    (2, 8),
    (4, 64),
    (8, 320),
    (16, 1280)
])
def test_recurrence_4_3_7_values(n, expected):
    assert recurrence_4_3_7(n) == expected
