"""
Mathematical proof (in English):

We want to prove that:
    ω(g(n)) ∩ o(g(n)) = ∅

Definitions:
- f(n) ∈ o(g(n)) means: for every constant c > 0, there exists n0 such that
  0 ≤ f(n) < c * g(n) for all n ≥ n0.
  This is a strict upper bound: f grows strictly slower than g.

- f(n) ∈ ω(g(n)) means: for every constant c > 0, there exists n0 such that
  0 ≤ c * g(n) < f(n) for all n ≥ n0.
  This is a strict lower bound: f grows strictly faster than g.

If a function f were in both o(g(n)) and ω(g(n)), it would have to grow
strictly slower and strictly faster than g(n) at the same time for large n,
which is impossible. Therefore, the intersection is empty.
"""

def is_little_o(f, g, n_values, epsilon=0.02):
    """
    Empirically check if f(n) = o(g(n)).
    This means f(n)/g(n) -> 0 as n -> infinity.
    We check that the ratio decreases and stays small for large n.
    """
    ratios = []
    for n in n_values:
        gv = g(n)
        if gv == 0:
            continue
        ratios.append(abs(f(n) / gv))
    if not ratios:
        return False
    tail = ratios[int(len(ratios) * 0.7):]  # last 30% of values
    # Check that all tail values are small and the last value is the smallest
    return max(tail) < epsilon and tail[-1] <= min(tail)


def is_little_omega(f, g, n_values, factor=100):
    """
    Empirically check if f(n) = ω(g(n)).
    This means f(n)/g(n) -> infinity as n -> infinity.
    We check that the ratio is large for large n.
    """
    ratios = []
    for n in n_values:
        gv = g(n)
        if gv == 0:
            continue
        ratios.append(abs(f(n) / gv))
    if not ratios:
        return False
    tail = ratios[int(len(ratios) * 0.7):]  # last 30% of values
    return all(r > factor for r in tail)

def intersection_nonempty(f, g, n_values):
    """
    Check if a function f could be both in o(g(n)) and ω(g(n)).
    Returns True if both conditions hold (should never happen for valid g).
    """
    return is_little_o(f, g, n_values) and is_little_omega(f, g, n_values)

if __name__ == "__main__":
    g_example = lambda n: n
    f_slower = lambda n: n**0.5
    f_faster = lambda n: n**2
    n_values_demo = range(10, 10000, 100)

    print("f_slower in o(g):", is_little_o(f_slower, g_example, n_values_demo))
    print("f_slower in ω(g):", is_little_omega(f_slower, g_example, n_values_demo))
    print("f_faster in o(g):", is_little_o(f_faster, g_example, n_values_demo))
    print("f_faster in ω(g):", is_little_omega(f_faster, g_example, n_values_demo))
