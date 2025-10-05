"""
Tests for Exercise 5.4-4
English: We check if the answer is 23.
Polish: Sprawdzamy, czy odpowiedź to 23.
"""

import pytest
from src.Chapter05.Exercise_5_4_4 import min_people_birthday_paradox

def test_min_people_birthday_paradox():
    assert min_people_birthday_paradox() == 23
