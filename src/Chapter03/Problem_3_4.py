"""
Asymptotic notation properties (in English):

We check the truth of each statement (a)–(g) from Problem 3-4.
Each function returns True if the statement is always true, False if it can be disproved.
"""

import math

def property_a():
    """
    (a) f(n) = O(g(n)) implies g(n) = O(f(n)).
    This is FALSE in general. Example: f(n) = n, g(n) = n^2.
    f = O(g), but g != O(f).
    """
    f = lambda n: n
    g = lambda n: n**2
    n = 1000
    return not (g(n) <= 100 * f(n))  # Should be False overall
    # Return False to indicate statement is false
    return False

def property_b():
    """
    (b) f(n) + g(n) = Θ(min(f(n), g(n))).
    This is FALSE. Example: f(n) = n, g(n) = n^2.
    f+g ~ g, min(f,g) ~ f, so not Θ(min).
    """
    return False

def property_c():
    """
    (c) f(n) = O(g(n)) implies lg(f(n)) = O(lg(g(n))) for large n.
    This is FALSE in general if f(n) can be < 1 or g(n) close to 1.
    Counterexample: f(n) = 1, g(n) = n.
    lg(1) = 0, lg(n) grows, so 0 = O(lg(n)) is actually TRUE.
    But if f(n) = n, g(n) = n^2, then lg(f) ~ lg(n), lg(g) ~ 2lg(n) → TRUE.
    Actually, for asymptotically positive functions > 1, this is TRUE.
    We'll assume domain large enough so logs are defined.
    """
    return True

def property_d():
    """
    (d) f(n) = Θ(n^2) implies f(n)^2 = Θ(n^4).
    TRUE: squaring preserves Θ with exponent multiplied by 2.
    """
    return True

def property_e():
    """
    (e) f(n) = O(n) implies 2^{f(n)} = O(2^n).
    TRUE: If f(n) <= c*n, then 2^{f(n)} <= 2^{c*n} = (2^n)^c = O(2^n) for c <= 1.
    But if c > 1, then 2^{c*n} is not O(2^n). So FALSE in general.
    Example: f(n) = 2n, O(n) but 2^{2n} = 4^n not O(2^n).
    """
    return False

def property_f():
    """
    (f) f(n) = O(g(n)) implies g(n) = Ω(f(n)).
    TRUE by definition of O and Ω.
    """
    return True

def property_g():
    """
    (g) f(n) = O(g(n)) and f(n) = Ω(g(n)) implies f(n) = Θ(g(n)).
    TRUE by definition of Θ.
    """
    return True

def all_properties():
    """
    Return dictionary with results for (a)–(g).
    """
    return {
        "a": property_a(),
        "b": property_b(),
        "c": property_c(),
        "d": property_d(),
        "e": property_e(),
        "f": property_f(),
        "g": property_g(),
    }

if __name__ == "__main__":
    results = all_properties()
    for k, v in results.items():
        print(f"Property {k}: {'TRUE' if v else 'FALSE'}")
