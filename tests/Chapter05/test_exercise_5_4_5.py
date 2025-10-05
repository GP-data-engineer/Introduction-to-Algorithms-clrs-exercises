"""
Tests for Exercise 5.4-5
English: We check if the answer mentions k=2.
Polish: Sprawdzamy, czy odpowiedź wspomina o k=2.
"""

import pytest
from src.Chapter05.Exercise_5_4_5 import kshow_relation

def test_kshow_relation():
    assert "k=2" in kshow_relation()
