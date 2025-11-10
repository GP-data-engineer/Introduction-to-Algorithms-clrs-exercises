"""
Testy do Problem 8.4 (PL): Sprawdzamy poprawność dopasowania dzbanków.
Tests for Problem 8.4 (EN): Verifies correct matching of jugs.
"""

import pytest
from src.Chapter08.Problem_8_4 import match_jugs

def test_jug_matching_correctness():
    red = [4, 2, 6, 8]
    blue = [2, 4, 8, 6]
    matched = match_jugs(red, blue)
    for r, b in matched:
        assert r == b

def test_jug_matching_length():
    red = [1, 3, 5]
    blue = [5, 1, 3]
    matched = match_jugs(red, blue)
    assert len(matched) == 3
