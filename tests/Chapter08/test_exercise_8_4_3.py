import pytest  
from src.Chapter08.Exercise_8_4_3 import expected_values

def test_expected_values():
    E_X, E_X2, E_X_squared = expected_values()
    assert pytest.approx(E_X) == 1.0
    assert pytest.approx(E_X2) == 1.5
    assert pytest.approx(E_X_squared) == 1.0
