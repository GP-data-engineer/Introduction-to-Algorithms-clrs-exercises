"""
Mathematical proof (in English):

We want to show:
The running time of an algorithm is Θ(g(n)) if and only if:
    - Its worst-case running time is O(g(n))
    - Its best-case running time is Ω(g(n))

Proof:

(=>) If T(n) = Θ(g(n)), then by definition there exist constants c1, c2 > 0 and n0 >= 0 such that:
    c1 * g(n) <= T(n) <= c2 * g(n) for all n >= n0.
    - The upper bound T(n) <= c2 * g(n) means worst-case time is O(g(n)).
    - The lower bound T(n) >= c1 * g(n) means best-case time is Ω(g(n)).

(<=) If worst-case time is O(g(n)) and best-case time is Ω(g(n)), then:
    - There exist c2 > 0, n1 >= 0: T_worst(n) <= c2 * g(n) for n >= n1
    - There exist c1 > 0, n2 >= 0: T_best(n) >= c1 * g(n) for n >= n2
    Taking n0 = max(n1, n2), we have:
        c1 * g(n) <= T_best(n) <= T_worst(n) <= c2 * g(n)
    Thus T(n) = Θ(g(n)).
"""

def is_big_o(f, g, n_values, tolerance=1e6):
    """Check if f(n) = O(g(n)) empirically."""
    ratios = []
    for n in n_values:
        gv = g(n)
        if gv == 0:
            continue
        ratios.append(f(n) / gv)
    if not ratios:
        return False
    if max(ratios) >= tolerance:
        return False
    if ratios[-1] > ratios[0] * 10:
        return False
    return True

def is_big_omega(f, g, n_values, tolerance=1e-6):
    """Check if f(n) = Ω(g(n)) empirically."""
    ratios = []
    for n in n_values:
        gv = g(n)
        if gv == 0:
            continue
        ratios.append(f(n) / gv)
    if not ratios:
        return False
    if min(ratios) <= tolerance:
        return False
    if ratios[-1] < ratios[0] / 10:
        return False
    return True

def satisfies_theorem(best_case_func, worst_case_func, g, n_values):
    """
    Check if the algorithm's running time satisfies:
    Θ(g(n)) <=> best-case = Ω(g(n)) and worst-case = O(g(n))
    """
    return is_big_omega(best_case_func, g, n_values) and is_big_o(worst_case_func, g, n_values)

if __name__ == "__main__":
    # Demonstration
    g_example = lambda n: n**2
    best_case = lambda n: 0.5 * n**2
    worst_case = lambda n: 3 * n**2 + 5 * n
    n_values_demo = range(10, 1000)

    print("Best-case is Ω(g(n)):", is_big_omega(best_case, g_example, n_values_demo))
    print("Worst-case is O(g(n)):", is_big_o(worst_case, g_example, n_values_demo))
    print("Satisfies theorem:", satisfies_theorem(best_case, worst_case, g_example, n_values_demo))
