import pytest
from src.Chapter06.Exercise_6_2_3 import max_heapify_no_change

def test_max_heapify_no_change():
    assert "No change" in max_heapify_no_change()
