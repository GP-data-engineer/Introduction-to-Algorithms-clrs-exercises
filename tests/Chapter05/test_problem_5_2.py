"""
Tests for Problem 5-2
English:
We check expected and worst-case times for RANDOM-SEARCH, DETERMINISTIC-SEARCH, and SCRAMBLE-SEARCH.
Polish:
Sprawdzamy oczekiwane i pesymistyczne czasy dla RANDOM-SEARCH, DETERMINISTIC-SEARCH i SCRAMBLE-SEARCH.
"""

import pytest
from src.Chapter05.Problem_5_2 import (
    expected_random_search, worst_random_search,
    expected_deterministic_search, worst_deterministic_search,
    expected_scramble_search, worst_scramble_search
)

def test_random_search_expectations():
    assert expected_random_search(10) == 10
    assert worst_random_search(10) == 10

def test_deterministic_search_expectations():
    assert expected_deterministic_search(9) == 5
    assert worst_deterministic_search(9) == 9

def test_scramble_search_expectations():
    assert expected_scramble_search(10, 1) == (10+1)/2
    assert expected_scramble_search(10, 0) == 10
    assert worst_scramble_search(10, 1) == 10
