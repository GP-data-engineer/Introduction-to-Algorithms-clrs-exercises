# Unit tests for Exercise 4.4.3
# Verifies correctness of recurrence_4_4_3 implementation

import pytest
from src.Chapter04.Exercise_4_4_3 import recurrence_4_4_3

@pytest.mark.parametrize("n,expected", [
    (1, 1),
    (2, 4 * 1 + 2),           # T(2) = 6
    (4, 4 * recurrence_4_4_3(2) + 4),
    (8, 4 * recurrence_4_4_3(4) + 8),
])
def test_recurrence_4_4_3_values(n, expected):
    assert recurrence_4_4_3(n) == expected
