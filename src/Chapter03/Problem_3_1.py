"""
Asymptotic behavior of polynomials (in English):

Given:
    p(n) = sum_{i=0}^d a_i * n^i, with a_d > 0
    k is a constant

We want to prove:
(a) If k > d, then p(n) = O(n^k)
(b) If k < d, then p(n) = Ω(n^k)
(c) If k = d, then p(n) = Θ(n^k)
(d) If k > d, then p(n) != Ω(n^k)
(e) If k < d, then p(n) != O(n^k)
(f) If k != d, then p(n) != Θ(n^k)

This module provides functions to empirically check these properties.
"""

def polynomial(n, coefficients):
    """
    Evaluate polynomial p(n) = sum_{i=0}^d a_i * n^i
    coefficients: list of a_i, where index i corresponds to power of n
    """
    return sum(coeff * (n ** i) for i, coeff in enumerate(coefficients))

def degree(coefficients):
    """
    Return the degree of the polynomial (highest i with non-zero coefficient).
    """
    for i in range(len(coefficients) - 1, -1, -1):
        if coefficients[i] != 0:
            return i
    return 0

def is_big_o(f, g, n_values, c=1.0):
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

def is_big_omega(f, g, n_values, c=1.0):
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

def is_big_theta(f, g, n_values, c1=1.0, c2=1.0):
    """
    Check if f(n) = Θ(g(n)) empirically.
    """
    return is_big_o(f, g, n_values, c2) and is_big_omega(f, g, n_values, c1)

if __name__ == "__main__":
    # Demonstration
    coeffs = [1, 0, 3]  # p(n) = 1 + 3n^2, degree d = 2
    d = degree(coeffs)
    k_values = [1, 2, 3]
    n_vals = range(50, 500, 50)

    for k in k_values:
        g = lambda n: n ** k
        p = lambda n: polynomial(n, coeffs)
        print(f"Degree d={d}, k={k}")
        print("O:", is_big_o(p, g, n_vals, c=10))
        print("Ω:", is_big_omega(p, g, n_vals, c=0.1))
        print("Θ:", is_big_theta(p, g, n_vals, c1=0.1, c2=10))
        print()
