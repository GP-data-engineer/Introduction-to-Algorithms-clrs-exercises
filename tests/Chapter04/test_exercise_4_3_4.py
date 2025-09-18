# Unit tests for Exercise 4.3-4
# Verifies correctness of recurrence_4_3_4 implementation

import pytest
from src.Chapter04.Exercise_4_3_4 import recurrence_4_3_4

@pytest.mark.parametrize("n,expected", [
    (1, 1),
    (2, 4),
    (4, 12),
    (8, 32),
    (16, 80)
])
def test_recurrence_4_3_4_values(n, expected):
    assert recurrence_4_3_4(n) == expected
