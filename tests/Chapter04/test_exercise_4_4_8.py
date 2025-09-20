# Unit tests for Exercise 4.4.8
# Verifies correctness of recurrence_4_4_8 implementation

import pytest
from src.Chapter04.Exercise_4_4_8 import recurrence_4_4_8

@pytest.mark.parametrize("n", [2, 4, 8])
def test_recurrence_4_4_8_growth(n):
    # Ensure logarithmic growth: T(n) > T(n-1)
    assert recurrence_4_4_8(n) > recurrence_4_4_8(n - 1)
