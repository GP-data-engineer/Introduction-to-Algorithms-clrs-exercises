# Unit tests for Exercise 4.4.4
# Verifies correctness of recurrence_4_4_4 implementation

import pytest
from src.Chapter04.Exercise_4_4_4 import recurrence_4_4_4

@pytest.mark.parametrize("n", [1, 4, 16, 64])
def test_recurrence_4_4_4_monotonic_growth(n):
    # Ensure function returns positive and increasing values
    assert recurrence_4_4_4(n) > 0
    assert recurrence_4_4_4(n) <= recurrence_4_4_4(n * 4)
