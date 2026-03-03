import pytest
from src.Chapter11.Exercise_11_4_4 import positions_checked

def test_positions_checked():
    assert positions_checked(12, 4) == 3
    assert positions_checked(11, 3) == 11
