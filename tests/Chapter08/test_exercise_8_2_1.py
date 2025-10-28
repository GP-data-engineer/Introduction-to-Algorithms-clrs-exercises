# test_exercise_8_2_1.py
import pytest
from src.Chapter06 import Exercise_8_2_1 as ex

def test_counting_sort_trace_and_result():
    A = [6, 0, 2, 0, 1, 3, 4, 6, 1, 3, 2]
    k = max(A)
    B, C, trace = ex.counting_sort_with_trace(A, k)
    # Correct sorted result
    assert B == sorted(A)
    # Final C should equal prefix sums: last element equals len(A)
    assert C[-1] == len(A)
    # Trace length should be >= number of placements + prefixes (sanity)
    assert len(trace) >= len(A) + 2
