# test_exercise_8_2_3.py
import pytest
from src.Chapter06 import Exercise_8_2_3 as ex

def test_left_to_right_produces_sorted():
    keys = [2, 0, 2, 1, 3, 1, 2]
    k = max(keys)
    B = ex.counting_sort_left_to_right(keys, k)
    assert B == sorted(keys)

def test_left_to_right_not_stable_example():
    # Construct an example where left-to-right variant breaks stability
    keys = [2, 2, 2]  # with payloads [a,b,c], left-to-right will reverse order of equal keys sometimes
    # To detect instability we use utility defined in module
    k = max(keys)
    stable = ex.is_stable_left_to_right([2, 2, 2], k)
    # For all-equal keys, left-to-right placement will keep relative order actually;
    # need mixed example to demonstrate non-stability. Use example below:
    keys2 = [1, 2, 1, 2, 1]  # there are several identical keys
    k2 = max(keys2)
    stable2 = ex.is_stable_left_to_right(keys2, k2)
    # We expect that variant can be unstable for some inputs.
    assert stable2 is False or stable2 is True  # sanity: function runs
    # stronger check: verify algorithm can be unstable by constructing scenario where indices do not stay sorted
    # We'll assert that for keys2 it is False (known counterexample)
    assert stable2 is False
