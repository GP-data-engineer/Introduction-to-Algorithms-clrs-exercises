#!/usr/bin/env python3
# test_exercise_2_2_1.py
"""
Tests for Exercise_2_2_1.py
"""

import Chapter02.Exercise_2_2_1 as ex


def test_function_growth():
    """
    The output of analyze_function should confirm that n^3 dominates for large n.
    Here we test values directly.
    """
    for n in [1000, 5000, 10000]:
        fn_value = (n**3) - 100*(n**2) - 100*n + 3
        # n^3 term should be much larger than n^2 term
        assert abs(fn_value) > abs(100*(n**2))


def test_theta_classification_docstring():
    """
    The prove_theta function's docstring should state Θ(n³) classification.
    """
    doc = ex.prove_theta.__doc__
    assert "Θ(n³)" in doc or "Theta(n³)" in doc or "theta(n³)" in doc
