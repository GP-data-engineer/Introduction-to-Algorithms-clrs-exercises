"""
Tests for Problem 4-5
We check if the simulation correctly finds a good circuit and identifies all good circuits.
"""

import pytest
from src.Chapter04.Problem_4_5 import Circuit, find_good_circuit, identify_all_good

def test_find_good_circuit_majority_good():
    # 6 good, 4 bad -> majority good
    circuits = [Circuit(True) for _ in range(6)] + [Circuit(False) for _ in range(4)]
    good_one = find_good_circuit(circuits)
    # The returned circuit must be good
    assert good_one.is_good is True

def test_identify_all_good():
    # 7 good, 3 bad
    circuits = [Circuit(True) for _ in range(7)] + [Circuit(False) for _ in range(3)]
    good_list = identify_all_good(circuits)
    # All good circuits should be identified
    assert all(c.is_good for c in good_list)
    assert len(good_list) == 7

def test_single_good_circuit():
    # Only one circuit, which is good
    circuits = [Circuit(True)]
    good_one = find_good_circuit(circuits)
    assert good_one.is_good is True
    good_list = identify_all_good(circuits)
    assert len(good_list) == 1
    assert good_list[0].is_good is True
