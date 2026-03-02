import pytest
from src.Chapter11.Exercise_11_4_3 import expected_probes

def test_expected_probes():
    s, f = expected_probes(0.75)
    assert f > s
