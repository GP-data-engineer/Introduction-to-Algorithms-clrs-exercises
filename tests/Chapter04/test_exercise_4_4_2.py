# Unit tests for Exercise 4.4.2
# Verifies correctness of recurrence_4_4_2 implementation

import pytest
from src.Chapter04.Exercise_4_4_2 import recurrence_4_4_2

@pytest.mark.parametrize("n,expected", [
    (1, 1),
    (2, 2 * 1 + 2),           # T(2) = 2*T(1) + 2 = 4
    (4, 2 * recurrence_4_4_2(2) + 4),
    (8, 2 * recurrence_4_4_2(4) + 8),
])
def test_recurrence_4_4_2_values(n, expected):
    assert recurrence_4_4_2(n) == expected
