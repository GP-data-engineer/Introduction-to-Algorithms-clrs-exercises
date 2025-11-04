# test_exercise_8_1_1.py 
import pytest
from src.Chapter08 import Exercise_8_1_1 as ex
import math

def test_lower_bound_height_small():
    assert ex.lower_bound_height(0) == 0
    assert ex.lower_bound_height(1) == 0
    # n=2 -> 2! = 2 -> ceil(log2 2) = 1
    assert ex.lower_bound_height(2) == 1

def test_lower_bound_matches_log2_factorial():
    for n in [3, 5, 8, 10]:
        h = ex.lower_bound_height(n)
        lb = ex.lower_bound_comparisons(n)
        # integer ceil of log2 should equal height
        assert h == math.ceil(lb)
