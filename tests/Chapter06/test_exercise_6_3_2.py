import pytest
from src.Chapter06.Exercise_6_3_2 import build_heap_loop_reason

def test_build_heap_loop_reason():
    assert "children" in build_heap_loop_reason()
