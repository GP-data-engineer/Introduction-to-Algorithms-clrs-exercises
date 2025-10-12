import pytest
from src.Chapter07.Exercise_7_1_3 import partition_average_case

def test_partition_average_case():
    assert "Θ(n)" in partition_average_case()
