# Unit tests for Exercise 4.3-5
# Verifies correctness of adjusted_inductive_hypothesis implementation

import pytest
from src.Chapter04.Exercise_4_3_5 import adjusted_inductive_hypothesis

@pytest.mark.parametrize("n,expected", [
    (1, 1),
    (2, 4),
    (4, 12),
    (8, 32),
    (16, 80)
])
def test_adjusted_inductive_hypothesis(n, expected):
    assert adjusted_inductive_hypothesis(n) == expected
