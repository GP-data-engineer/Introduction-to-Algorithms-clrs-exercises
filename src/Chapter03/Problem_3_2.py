"""
Relative asymptotic order (in English):

Given pairs of functions (A, B), determine whether:
- A ∈ O(B)
- A ∈ o(B)
- A ∈ Ω(B)
- A ∈ ω(B)
- A ∈ Θ(B)

We use empirical checks for large n to approximate the relationships.
"""

import math

def is_big_o(f, g, n_values, c=1e6):
    """
    Check if f(n) = O(g(n)) empirically.
    """
    for n in n_values:
        gv = g(n)
        if gv == 0:
            continue
        if f(n) > c * gv:
            return False
    return True

def is_little_o(f, g, n_values, epsilon=1e-6):
    """
    Check if f(n) = o(g(n)) empirically.
    """
    ratios = []
    for n in n_values:
        gv = g(n)
        if gv == 0:
            continue
        ratios.append(abs(f(n) / gv))
    if not ratios:
        return False
    return max(ratios) < epsilon

def is_big_omega(f, g, n_values, c=1e-6):
    """
    Check if f(n) = Ω(g(n)) empirically.
    """
    for n in n_values:
        gv = g(n)
        if gv == 0:
            continue
        if f(n) < c * gv:
            return False
    return True

def is_little_omega(f, g, n_values, factor=1e6):
    """
    Check if f(n) = ω(g(n)) empirically.
    """
    ratios = []
    for n in n_values:
        gv = g(n)
        if gv == 0:
            continue
        ratios.append(abs(f(n) / gv))
    if not ratios:
        return False
    return min(ratios) > factor

def is_big_theta(f, g, n_values, c1=1e-6, c2=1e6):
    """
    Check if f(n) = Θ(g(n)) empirically.
    """
    return is_big_o(f, g, n_values, c2) and is_big_omega(f, g, n_values, c1)

def analyze_pair(f, g, n_values):
    """
    Return a dict with results for O, o, Ω, ω, Θ.
    """
    return {
        "O": is_big_o(f, g, n_values),
        "o": is_little_o(f, g, n_values),
        "Omega": is_big_omega(f, g, n_values),
        "omega": is_little_omega(f, g, n_values),
        "Theta": is_big_theta(f, g, n_values)
    }

if __name__ == "__main__":
    # Example demonstration
    n_vals = [10**k for k in range(2, 6)]
    pairs = [
        (lambda n: n, lambda n: n**2),
        (lambda n: math.sqrt(n), lambda n: n**math.sin(1)),
        (lambda n: n**0.5, lambda n: math.log(n)),
    ]
    for idx, (f, g) in enumerate(pairs, start=1):
        print(f"Pair {idx}:", analyze_pair(f, g, n_vals))
