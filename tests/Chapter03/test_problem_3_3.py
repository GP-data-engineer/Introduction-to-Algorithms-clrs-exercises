"""
Tests for Problem 3-3.
"""

import math
import pytest
from src.Chapter03.Problem_3_3 import get_ordered_functions, get_equivalence_classes, example_function_part_b, safe_value

def test_ordering_is_sorted_for_large_n():
    """Verify that the returned ordering is non-increasing for large n."""
    funcs = get_ordered_functions()
    n = 50
    values = [safe_value(desc, n) for desc, _ in funcs]
    for a, b in zip(values, values[1:]):
        assert a >= b

def test_equivalence_classes_are_constant_factors():
    """Verify that functions in the same Θ-class differ only by a constant factor for large n."""
    classes = get_equivalence_classes()
    n = 1000
    funcs_dict = dict(get_ordered_functions())
    for eq_class in classes:
        for i in range(len(eq_class) - 1):
            fa = funcs_dict[eq_class[i]]
            fb = funcs_dict[eq_class[i + 1]]
            ratio = fa(n) / fb(n)
            assert ratio > 0
            assert math.isclose(ratio, ratio, rel_tol=0.5)

def test_example_function_part_b_behavior():
    """
    The example function alternates between small and large growth,
    so it should not be O or Ω of any monotonic function from part (a).
    """
    f = example_function_part_b()
    funcs = get_ordered_functions()
    n_values = range(10, 30)
    for desc, g in funcs:
        less_count = sum(1 for n in n_values if f(n) <= g(n))
        greater_count = sum(1 for n in n_values if f(n) >= g(n))
        assert less_count > 0 and greater_count > 0
