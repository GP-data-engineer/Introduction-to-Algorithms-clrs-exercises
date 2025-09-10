"""
Tests for Exercise 3.2-6.
We test factorial vs exponential growth and asymptotic analysis.
"""

import pytest
from src.Chapter03.Exercise_3_2_6 import compare_factorial_growth, analyze_pair


def test_factorial_growth():
    """Test that n! grows faster than 2^n for n in range 3..9."""
    for n in range(3, 10):
        greater, smaller = compare_factorial_growth(n)
        assert greater is True
        assert smaller is False


def test_n_vs_n_squared():
    """
    Test that n grows slower than n^2:
    - O and o should be True
    - Ω, ω, Θ should be False
    """
    n_vals = [10**k for k in range(2, 6)]
    result = analyze_pair(lambda n: n, lambda n: n**2, n_vals)
    assert result["O"] is True
    assert result["o"] is True
    assert result["Ω"] is False
    assert result["ω"] is False
    assert result["Θ"] is False


if __name__ == "__main__":
    # Run tests manually if executed directly
    print("Running tests for Exercise 3.2-6...\n")
    pytest.main([__file__])

