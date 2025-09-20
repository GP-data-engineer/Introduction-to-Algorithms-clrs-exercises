# Unit tests for Exercise 4.4.9
# Verifies correctness of recurrence_4_4_9 implementation

import pytest
from src.Chapter04.Exercise_4_4_9 import recurrence_4_4_9

@pytest.mark.parametrize("n", [2, 4, 8])
def test_recurrence_4_4_9_structure(n):
    # Check recurrence matches expected recursive structure
    assert recurrence_4_4_9(n) == (
        recurrence_4_4_9(n - 1) +
        recurrence_4_4_9(n // 2) +
        n
    )
