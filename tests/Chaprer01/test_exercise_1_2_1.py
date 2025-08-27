#!/usr/bin/env python3
# test_exercise_1_2_1.py
"""
Tests for Exercise_1_2_1.py
"""

import Exercise_1_2_1 as ex

def test_description_contains_keywords():
    desc = ex.description().lower()
    for keyword in ["indexing", "hashing", "graph search", "sorting", "similarity"]:
        assert keyword in desc
