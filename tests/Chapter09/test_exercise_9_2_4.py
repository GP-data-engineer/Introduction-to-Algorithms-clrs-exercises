# Test for Exercise 9.2-4 (EN): Verifies worst-case trace of RANDOMIZED-SELECT.
# Test do Exercise 9.2-4 (PL): Sprawdza przebieg pesymistyczny RANDOMIZED-SELECT.

import pytest
from src.Chapter09.Exercise_9_2_4 import worst_case_randomized_select_trace

def test_trace_length():
    A = [3, 2, 9, 0, 7, 5, 4, 8, 6, 1]
    trace = worst_case_randomized_select_trace(A.copy(), 1)
    assert len(trace) == len(A)

def test_trace_pivots_descending():
    A = [3, 2, 9, 0, 7, 5, 4, 8, 6, 1]
    trace = worst_case_randomized_select_trace(A.copy(), 1)
    pivots = [pivot for _, pivot in trace]
    assert pivots == [max(step) for step, _ in trace]
