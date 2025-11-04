# test_exercise_8_3_5.py 
import pytest
from src.Chapter08 import Exercise_8_3_5 as ex

def test_phases_and_piles_basic():
    phases, piles = ex.phases_and_piles_for_decimal(5)
    assert phases == 5
    assert piles == 10

def test_simulate_piles_length():
    arr = [170, 45, 75, 90, 802, 24, 2, 66]
    history = ex.simulate_radix_piles_decimal(arr, 3)
    # should have 3 passes
    assert len(history) == 3
    # each pass piles length list should have size 10
    for entry in history:
        assert len(entry) == 10
