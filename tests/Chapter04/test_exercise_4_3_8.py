# Unit tests for Exercise 4.3-8
# Verifies correctness of recurrence_4_3_8 implementation

import pytest
from src.Chapter04.Exercise_4_3_8 import recurrence_4_3_8

@pytest.mark.parametrize("n,expected", [
    (1, 1),
    (2, 6),
    (4, 28),
    (8, 120),
    (16, 496)
])
def test_recurrence_4_3_8_values(n, expected):
    assert recurrence_4_3_8(n) == expected
