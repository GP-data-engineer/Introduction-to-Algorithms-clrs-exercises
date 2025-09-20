# Unit tests for Exercise 4.4.5
# Verifies correctness of recurrence_4_4_5 implementation

import pytest
from src.Chapter04.Exercise_4_4_5 import recurrence_4_4_5

@pytest.mark.parametrize("n", [1, 2, 4, 6])
def test_recurrence_4_4_5_growth(n):
    # Ensure function returns increasing values
    assert recurrence_4_4_5(n) >= recurrence_4_4_5(n - 2)
