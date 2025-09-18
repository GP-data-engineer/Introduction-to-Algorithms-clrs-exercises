# Unit tests for Exercise 4.3-6
# Verifies correctness of merge_sort_recurrence implementation

import pytest
from src.Chapter04.Exercise_4_3_6 import merge_sort_recurrence

@pytest.mark.parametrize("n,expected", [
    (1, 1),
    (2, 4),
    (4, 12),
    (8, 32),
    (16, 80)
])
def test_merge_sort_recurrence(n, expected):
    assert merge_sort_recurrence(n) == expected
