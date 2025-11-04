# test_exercise_8_3_2.py 
import pytest
from src.Chapter08 import Exercise_8_3_2 as ex

def test_stability_answers_format():
    ans = ex.answers()
    assert 'insertion_sort' in ans and 'merge_sort' in ans and 'heap_sort' in ans and 'quicksort' in ans

def test_make_stable_by_index_preserves_order_for_equals():
    arr = [(2,'a'), (1,'b'), (2,'c'), (1,'d'), (2,'e')]
    sorted_arr = ex.make_stable_by_index(arr)
    # for keys==2, payload order should be ['a','c','e']
    two_payloads = [payload for key,payload in sorted_arr if key==2]
    assert two_payloads == ['a','c','e']
    # for keys==1, order should be ['b','d']
    one_payloads = [payload for key,payload in sorted_arr if key==1]
    assert one_payloads == ['b','d']
