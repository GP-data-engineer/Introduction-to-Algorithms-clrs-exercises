# test_exercise_8_3_4.py
import pytest
import random
from src.Chapter06 import Exercise_8_3_4 as ex

def test_sort_numbers_range_and_correctness():
    for n in [1, 2, 5, 10, 50]:
        random.seed(0)
        A = [random.randint(0, n**3 - 1) for _ in range(n)]
        B = ex.sort_numbers_0_to_n3_minus1(A)
        assert B == sorted(A)

def test_invalid_input_raises():
    A = [0, 1, 2]
    # n = len(A) = 3, range is 0..26, value 27 should raise
    with pytest.raises(ValueError):
        ex.sort_numbers_0_to_n3_minus1([0, 27, 5])
