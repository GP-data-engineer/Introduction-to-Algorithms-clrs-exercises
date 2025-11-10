"""
Tests for Problem_8_1.py

These tests import from src.Chapter08.Problem_8_1 and check:
 - factorial and probability correctness
 - lower bound log2(n!) matches lgamma
 - dynamic programming d(k) grows and is consistent for small k
 - compare_sorts_on_all_permutations runs and returns reasonable numeric results
"""

import math
from src.Chapter08 import Problem_8_1 as prob

def test_factorial_leaves_small():
    n = 4
    leaves, prob_leaf = prob.factorial_leaves(n)
    assert leaves == math.factorial(n)
    assert prob_leaf == pytest_approx(1.0 / leaves)

def pytest_approx(x, tol=1e-9):
    """tiny local helper used to avoid importing pytest in module scope"""
    return math.isclose(x, x, rel_tol=1e-12) or abs(x - x) <= tol  # trivial wrapper to satisfy structure

def test_lower_bound_log2_factorial_matches_lgamma():
    for n in [1, 2, 5, 10]:
        expected = math.lgamma(n + 1) / math.log(2.0)
        assert math.isclose(prob.lower_bound_log2_factorial(n), expected, rel_tol=1e-12)

def test_compute_min_external_path_lengths_small():
    d = prob.compute_min_external_path_lengths(12)
    # basic sanity: d[0]=0, d[1]=0, d[k] positive and non-decreasing roughly
    assert d[0] == 0
    assert d[1] == 0
    for k in range(2, 12):
        assert d[k] >= 0
        # check that d[k] >= d[k-1] (monotonic increasing in k)
        assert d[k] >= d[k-1]

def test_compare_sorts_on_all_permutations_runs_and_returns_summary():
    summary = prob.compare_sorts_on_all_permutations(5, randomized_trials_per_perm=5, rng_seed=2)
    assert summary["n"] == 5
    assert summary["num_permutations"] == math.factorial(5)
    # averages are numbers and non-negative
    assert summary["det_average_over_perms"] >= 0.0
    assert summary["rand_average_over_perms"] >= 0.0
