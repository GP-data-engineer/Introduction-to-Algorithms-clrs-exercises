"""
Mathematical definitions (in English):

We extend asymptotic notation to functions of two parameters n and m.

Definition:
O(g(n, m)) = { f(n, m) : there exist positive constants c, n0, m0
such that 0 <= f(n, m) <= c * g(n, m) for all n >= n0 and m >= m0 }

Analogous definitions:

Ω(g(n, m)) = { f(n, m) : there exist positive constants c, n0, m0
such that 0 <= c * g(n, m) <= f(n, m) for all n >= n0 and m >= m0 }

Θ(g(n, m)) = O(g(n, m)) ∩ Ω(g(n, m))
"""

def is_big_o_2d(f, g, n_values, m_values, c=1.0):
    """
    Empirically check if f(n, m) = O(g(n, m)).
    We check that f(n, m) <= c * g(n, m) for all sufficiently large n, m.
    """
    for n in n_values:
        for m in m_values:
            gv = g(n, m)
            if gv == 0:
                continue
            if f(n, m) > c * gv:
                return False
    return True

def is_big_omega_2d(f, g, n_values, m_values, c=1.0):
    """
    Empirically check if f(n, m) = Ω(g(n, m)).
    We check that f(n, m) >= c * g(n, m) for all sufficiently large n, m.
    """
    for n in n_values:
        for m in m_values:
            gv = g(n, m)
            if gv == 0:
                continue
            if f(n, m) < c * gv:
                return False
    return True

def is_big_theta_2d(f, g, n_values, m_values, c1=1.0, c2=1.0):
    """
    Empirically check if f(n, m) = Θ(g(n, m)).
    This means f(n, m) is both O(g(n, m)) and Ω(g(n, m)).
    """
    return is_big_o_2d(f, g, n_values, m_values, c2) and \
           is_big_omega_2d(f, g, n_values, m_values, c1)

if __name__ == "__main__":
    # Demonstration
    g_example = lambda n, m: n * m
    f_same = lambda n, m: 3 * n * m
    f_slower = lambda n, m: n * m**0.5
    f_faster = lambda n, m: n**2 * m**2

    n_vals = range(50, 200, 50)
    m_vals = range(50, 200, 50)

    print("f_same is Θ(g):", is_big_theta_2d(f_same, g_example, n_vals, m_vals))
    print("f_slower is O(g):", is_big_o_2d(f_slower, g_example, n_vals, m_vals))
    print("f_faster is Ω(g):", is_big_omega_2d(f_faster, g_example, n_vals, m_vals))
