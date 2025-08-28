import pytest
from src.Chapter02.Exercise_2_2_3 import linear_search_analysis

def test_linear_search_analysis_small():
    result = linear_search_analysis(5)
    assert result["average_checks"] == 3
    assert result["worst_checks"] == 5
    assert result["average_case_time"] == "Θ(n)"
    assert result["worst_case_time"] == "Θ(n)"

def test_linear_search_analysis_large():
    result = linear_search_analysis(100)
    assert result["average_checks"] == 50.5
    assert result["worst_checks"] == 100
