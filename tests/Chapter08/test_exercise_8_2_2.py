# test_exercise_8_2_2.py 
import pytest
from src.Chapter08 import Exercise_8_2_2 as ex

def test_counting_sort_stability_on_example():
    keys = [2, 5, 3, 2, 3, 5, 2]
    k = max(keys)
    # verify that implementation is stable
    assert ex.is_stable_counting_sort(keys, k) is True

def test_counting_sort_returns_sorted_pairs():
    A = [(2, 'a'), (1, 'b'), (2, 'c'), (0, 'd')]
    k = max(key for key, _ in A)
    B = ex.counting_sort_stable(A, k)
    # keys should be sorted
    assert [k for k, _ in B] == sorted(k for k, _ in A)
    # check stability: for keys==2 payloads order should be 'a' then 'c'
    two_payloads = [payload for key, payload in B if key == 2]
    assert two_payloads == ['a', 'c']
