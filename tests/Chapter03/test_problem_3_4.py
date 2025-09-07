# Tests for Problem 3-4: Properties of asymptotic notation
# This test suite verifies the truth or falsity of seven statements (a)–(g)
# about asymptotic notation for asymptotically positive functions f(n) and g(n).
# Each property is implemented in Problem_3_4.py as a separate function returning
# True if the statement is always true, or False if it can be disproved.
# The tests check each property individually and also verify the combined results
# returned by all_properties().

import pytest
from src.Chapter03.Problem_3_4 import (
    property_a, property_b, property_c,
    property_d, property_e, property_f, property_g,
    all_properties
)

def test_property_a():
    # (a) f(n) = O(g(n)) implies g(n) = O(f(n))
    # This is false in general. Example: f(n) = n, g(n) = n^2.
    # f is O(g), but g is not O(f).
    assert property_a() is False

def test_property_b():
    # (b) f(n) + g(n) = Θ(min(f(n), g(n)))
    # This is false. Example: f(n) = n, g(n) = n^2.
    # f+g ~ g, min(f,g) ~ f, so they are not Θ-equivalent.
    assert property_b() is False

def test_property_c():
    # (c) f(n) = O(g(n)) implies lg(f(n)) = O(lg(g(n))) for large n
    # This is true for asymptotically positive functions > 1.
    assert property_c() is True

def test_property_d():
    # (d) f(n) = Θ(n^2) implies f(n)^2 = Θ(n^4)
    # This is true: squaring preserves Θ with exponent multiplied by 2.
    assert property_d() is True

def test_property_e():
    # (e) f(n) = O(n) implies 2^{f(n)} = O(2^n)
    # This is false in general. Example: f(n) = 2n is O(n),
    # but 2^{2n} = 4^n is not O(2^n).
    assert property_e() is False

def test_property_f():
    # (f) f(n) = O(g(n)) implies g(n) = Ω(f(n))
    # This is true by the definition of O and Ω.
    assert property_f() is True

def test_property_g():
    # (g) f(n) = O(g(n)) and f(n) = Ω(g(n)) implies f(n) = Θ(g(n))
    # This is true by the definition of Θ.
    assert property_g() is True

def test_all_properties_dict():
    # Verify that all_properties() returns the expected dictionary
    # with correct truth values for each property (a)–(g).
    results = all_properties()
    assert results == {
        "a": False,
        "b": False,
        "c": True,
        "d": True,
        "e": False,
        "f": True,
        "g": True
    }
