"""
Tests for Exercise 5.4-1
English: We check if the computed minimum numbers of people are correct.
Polish: Sprawdzamy, czy obliczone minimalne liczby osób są poprawne.
"""

import pytest
from src.Chapter05.Exercise_5_4_1 import min_people_same_birthday_as_you, min_people_two_on_may3

def test_min_people_same_birthday_as_you():
    # Known result: 253 people needed
    assert min_people_same_birthday_as_you() == 253

def test_min_people_two_on_may3():
    # Known result: 612 people needed
    assert min_people_two_on_may3() == 612
