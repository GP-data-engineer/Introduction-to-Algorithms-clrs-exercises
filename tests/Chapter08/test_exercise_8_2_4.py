# test_exercise_8_2_4.py 
import pytest
import random
from src.Chapter08 import Exercise_8_2_4 as ex

def test_preprocessor_basic_queries():
    A = [2, 5, 3, 2, 0, 10, 7, 5, 3, 2]
    k = 10
    cp = ex.CountingPreprocessor()
    cp.build(A, k)
    assert cp.query(0, 2) == sum(1 for x in A if 0 <= x <= 2)
    assert cp.query(2, 3) == sum(1 for x in A if 2 <= x <= 3)
    assert cp.query(4, 6) == sum(1 for x in A if 4 <= x <= 6)
    assert cp.query(0, 10) == len(A)
    # query with out of range bounds
    assert cp.query(-5, 1) == sum(1 for x in A if 0 <= x <= 1)
    assert cp.query(8, 20) == sum(1 for x in A if 8 <= x <= 10)

def test_preprocessor_randomized():
    random.seed(0)
    n = 1000
    k = 50
    A = [random.randint(0, k) for _ in range(n)]
    cp = ex.CountingPreprocessor()
    cp.build(A, k)
    for _ in range(50):
        a = random.randint(-5, k+5)
        b = random.randint(-5, k+5)
        if a > b:
            a, b = b, a
        expected = sum(1 for x in A if a <= x <= b)
        assert cp.query(a, b) == expected
