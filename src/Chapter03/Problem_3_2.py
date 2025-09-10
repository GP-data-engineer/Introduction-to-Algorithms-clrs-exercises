""" Problem_3_2.py
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

def safe_ratio(f_val, g_val):
    """Return safe ratio f/g, handling zero and overflow."""
    if g_val == 0:
        return math.inf
    try:
        return f_val / g_val
    except OverflowError:
        return math.inf

def safe_eval(func, n):
    """Evaluate func(n) safely, catching overflow."""
    try:
        return func(n)
    except OverflowError:
        return math.inf

def is_big_o(f, g, n_values, factor_limit=1e6):
    """Check if f(n) = O(g(n)) empirically."""
    ratios = [safe_ratio(safe_eval(f, n), safe_eval(g, n)) for n in n_values]
    # If ratio is increasing significantly, it's not O
    if ratios[-1] > ratios[0] * 10:
        return False
    return max(ratios) < factor_limit

def is_little_o(f, g, n_values, small_threshold=0.1):
    """Check if f(n) = o(g(n)) empirically."""
    ratios = [safe_ratio(safe_eval(f, n), safe_eval(g, n)) for n in n_values]
    return ratios[-1] < small_threshold and ratios[-1] < ratios[0]

def is_big_omega(f, g, n_values, lower_limit=0.1):
    """Check if f(n) = Ω(g(n)) empirically."""
    ratios = [safe_ratio(safe_eval(f, n), safe_eval(g, n)) for n in n_values]
    # If ratio decreases significantly, it's not Ω
    if ratios[-1] < ratios[0] / 10:
        return False
    return min(ratios) > lower_limit

def is_little_omega(f, g, n_values, large_threshold=10):
    """Check if f(n) = ω(g(n)) empirically."""
    ratios = [safe_ratio(safe_eval(f, n), safe_eval(g, n)) for n in n_values]
    return ratios[-1] > large_threshold and ratios[-1] > ratios[0]

def is_big_theta(f, g, n_values):
    """Check if f(n) = Θ(g(n)) empirically."""
    return is_big_o(f, g, n_values) and is_big_omega(f, g, n_values)

def analyze_pair(f, g, n_values):
    """Return a dict with results for O, o, Ω, ω, Θ."""
    return {
        "O": is_big_o(f, g, n_values),
        "o": is_little_o(f, g, n_values),
        "Omega": is_big_omega(f, g, n_values),
        "omega": is_little_omega(f, g, n_values),
        "Theta": is_big_theta(f, g, n_values)
    }

if __name__ == "__main__":
    n_vals = [10**k for k in range(2, 6)]
    pairs = [
        ("n vs n^2", lambda n: n, lambda n: n**2),
        ("sqrt(n) vs n^sin(1)", lambda n: math.sqrt(n), lambda n: n**math.sin(1)),
        ("n^0.5 vs log(n)", lambda n: n**0.5, lambda n: math.log(n)),
        ("lg(n) vs (lg(n))^n", lambda n: math.log(n, 10), lambda n: math.exp(n * math.log(math.log(n, 10)))),
    ]
    for name, f, g in pairs:
        print(f"\n=== {name} ===")
        print(analyze_pair(f, g, n_vals))
