"""
Mathematical proof (in Polish):

Twierdzenie 3.1:
Dla każdych dwóch funkcji f(n) i g(n) zachodzi:
    f(n) = Θ(g(n))  <=>  f(n) = O(g(n)) i f(n) = Ω(g(n))

Dowód:

(=>) Jeśli f(n) = Θ(g(n)), to z definicji istnieją c1, c2 > 0 oraz n0, takie że:
    c1 * g(n) <= f(n) <= c2 * g(n)  dla n >= n0.
    Zatem:
        - f(n) <= c2 * g(n)  =>  f(n) = O(g(n))
        - f(n) >= c1 * g(n)  =>  f(n) = Ω(g(n))

(<=) Jeśli f(n) = O(g(n)) i f(n) = Ω(g(n)), to:
    - Istnieją c2 > 0, n1 >= 0: f(n) <= c2 * g(n) dla n >= n1
    - Istnieją c1 > 0, n2 >= 0: f(n) >= c1 * g(n) dla n >= n2
    Biorąc n0 = max(n1, n2), mamy:
        c1 * g(n) <= f(n) <= c2 * g(n) dla n >= n0
    Z definicji: f(n) = Θ(g(n))
"""

def is_big_o(f, g, n_values):
    """
    Checks if f(n) = O(g(n)) empirically for given n_values.
    """
    ratios = []
    for n in n_values:
        gv = g(n)
        if gv == 0:
            continue
        ratios.append(f(n) / gv)
    if not ratios:
        return False
    return max(ratios) < float('inf')

def is_big_omega(f, g, n_values):
    """
    Checks if f(n) = Ω(g(n)) empirically for given n_values.
    """
    ratios = []
    for n in n_values:
        gv = g(n)
        if gv == 0:
            continue
        ratios.append(f(n) / gv)
    if not ratios:
        return False
    return min(ratios) > 0

def is_big_theta(f, g, n_values):
    """
    Checks if f(n) = Θ(g(n)) empirically for given n_values.
    """
    return is_big_o(f, g, n_values) and is_big_omega(f, g, n_values)

if __name__ == "__main__":
    # Demonstration
    f_example = lambda n: 5 * n**2 + 3 * n + 1
    g_example = lambda n: n**2
    n_values_demo = range(10, 1000)

    print("f(n) = O(g(n)):", is_big_o(f_example, g_example, n_values_demo))
    print("f(n) = Ω(g(n)):", is_big_omega(f_example, g_example, n_values_demo))
    print("f(n) = Θ(g(n)):", is_big_theta(f_example, g_example, n_values_demo))
