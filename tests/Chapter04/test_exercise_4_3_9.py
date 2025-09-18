# Unit tests for Exercise 4.3-9
# Verifies correctness of recurrence_4_3_9 implementation

import pytest
from src.Chapter04.Exercise_4_3_9 import recurrence_4_3_9

@pytest.mark.parametrize("n,expected", [
    (1, 1),
    (2, 12),
    (4, 112),
    (8, 960),
    (16, 7936)
])
def test_recurrence_4_3_9_values(n, expected):
    assert recurrence_4_3_9(n) == expected
