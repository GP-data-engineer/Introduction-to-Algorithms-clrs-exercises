# Unit tests for Exercise 4.4.1
# Verifies correctness of recurrence_4_4_1 implementation

import pytest
from src.Chapter04.Exercise_4_4_1 import recurrence_4_4_1

@pytest.mark.parametrize("n,expected", [
    (1, 1),
    (2, 3 * 1 + 2),           # T(2) = 3*T(1) + 2 = 5
    (4, 3 * recurrence_4_4_1(2) + 4),  # T(4) = 3*T(2) + 4
    (8, 3 * recurrence_4_4_1(4) + 8),
])
def test_recurrence_4_4_1_values(n, expected):
    assert recurrence_4_4_1(n) == expected
