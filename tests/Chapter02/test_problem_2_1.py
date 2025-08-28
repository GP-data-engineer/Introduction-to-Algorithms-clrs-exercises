#!/usr/bin/env python3
# test_problem_2_1.py
"""
Tests for Problem_2_1.py
"""

import Chapter02.Problem_2_1 as problem


def test_max_n_for_time_increases_with_limit():
    """Check that larger time limits allow for larger n."""
    small_limit = 1_000
    large_limit = 1_000_000
    f = problem.functions["n^2"]
    n_small = problem.max_n_for_time(small_limit, f)
    n_large = problem.max_n_for_time(large_limit, f)
    assert n_large > n_small


def test_log_n_case():
    """For log n, even huge limits should allow very large n."""
    f = problem.functions["log n"]
    limit = problem.time_limits["1 century"]
    n_value = problem.max_n_for_time(limit, f)
    assert n_value > 10**10  # log n grows extremely slowly


def test_factorial_case():
    """For n!, max n should be small even for big limits."""
    f = problem.functions["n!"]
    limit = problem.time_limits["1 year"]
    n_value = problem.max_n_for_time(limit, f)
    assert n_value < 20
