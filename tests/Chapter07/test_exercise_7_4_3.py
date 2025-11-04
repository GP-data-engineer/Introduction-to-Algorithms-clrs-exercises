# test_exercise_7_4_3.py
# Tests for Exercise_7_4_3.py

from src.Chapter07 import Exercise_7_4_3 as ex

def test_quadratic_max_at_edges():
    for n in [2, 3, 5, 10, 20]:
        q, val, vals = ex.argmax_quadratic(n)
        # maximum value should be at q=0 or q=n-1 (both give same value)
        assert q == 0 or q == n - 1
        edge_val = vals[0]
        edge_val2 = vals[n - 1]
        assert val == edge_val or val == edge_val2
