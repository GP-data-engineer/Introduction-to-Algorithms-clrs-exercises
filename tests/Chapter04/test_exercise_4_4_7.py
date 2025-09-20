# Unit tests for Exercise 4.4.7
# Verifies correctness of recurrence_4_4_7 implementation

import pytest
from src.Chapter04.Exercise_4_4_7 import recurrence_4_4_7

@pytest.mark.parametrize("n", [3, 4, 5])
def test_recurrence_4_4_7_values(n):
    # Check recurrence matches expected sum of previous three terms
    assert recurrence_4_4_7(n) == (
        recurrence_4_4_7(n - 1) +
        recurrence_4_4_7(n - 2) +
        recurrence_4_4_7(n - 3)
    )
