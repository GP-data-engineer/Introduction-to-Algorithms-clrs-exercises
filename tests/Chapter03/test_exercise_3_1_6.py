import pytest
from src.Chapter03.Exercise_3_1_6 import is_big_o, is_big_omega, satisfies_theorem

def test_quadratic_case():
    """
    Positive case:
    Both best-case and worst-case have the same growth rate as g(n) = n^2.
    - best_case = 0.5 * n^2  => Ω(n^2)
    - worst_case = 3 * n^2 + 5n => O(n^2)
    Therefore, the theorem should be satisfied.
    """
    g = lambda n: n**2
    best_case = lambda n: 0.5 * n**2
    worst_case = lambda n: 3 * n**2 + 5 * n
    n_values = range(10, 1000)
    assert is_big_omega(best_case, g, n_values)
    assert is_big_o(worst_case, g, n_values)
    assert satisfies_theorem(best_case, worst_case, g, n_values)

def test_not_satisfying_theorem_due_to_worst_case():
    """
    Negative case:
    Worst-case grows faster than g(n) = n^2 (worst_case = n^3).
    - best_case = n^2 => Ω(n^2) (OK)
    - worst_case = n^3 => NOT O(n^2) (fails)
    Therefore, the theorem should NOT be satisfied.
    """
    g = lambda n: n**2
    best_case = lambda n: n**2
    worst_case = lambda n: n**3
    n_values = range(10, 1000)
    assert not is_big_o(worst_case, g, n_values)
    assert not satisfies_theorem(best_case, worst_case, g, n_values)

def test_not_satisfying_theorem_due_to_best_case():
    """
    Negative case:
    Best-case grows slower than g(n) = n^2 (best_case = n).
    - best_case = n => NOT Ω(n^2) (fails)
    - worst_case = n^2 => O(n^2) (OK)
    Therefore, the theorem should NOT be satisfied.
    """
    g = lambda n: n**2
    best_case = lambda n: n
    worst_case = lambda n: n**2
    n_values = range(10, 1000)
    assert not is_big_omega(best_case, g, n_values)
    assert not satisfies_theorem(best_case, worst_case, g, n_values)
