# Unit tests for Exercise 4.3-3
# Verifies correctness of recurrence_4_3_3 implementation

import pytest
from src.Chapter04.Exercise_4_3_3 import recurrence_4_3_3

@pytest.mark.parametrize("n,expected", [
    (1, 1),
    (2, 4),
    (4, 12),
    (8, 32),
    (16, 80)
])
def test_recurrence_4_3_3_values(n, expected):
    assert recurrence_4_3_3(n) == expected
