# Unit tests for Exercise 4.4.6
# Verifies correctness of recurrence_4_4_6 implementation

import pytest
from src.Chapter04.Exercise_4_4_6 import recurrence_4_4_6

@pytest.mark.parametrize("n", [2, 4, 8])
def test_recurrence_4_4_6_growth(n):
    # Ensure harmonic growth: T(n) > T(n-1)
    assert recurrence_4_4_6(n) > recurrence_4_4_6(n - 1)
