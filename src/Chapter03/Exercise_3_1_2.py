"""
Mathematical proof (in Polish):

Chcemy pokazać, że dla dowolnych rzeczywistych stałych a i b, gdzie b > 0:
    (n + a)^b = Θ(n^b)

Definicja Θ(h(n)):
    f(n) = Θ(h(n)) ⇔ istnieją stałe c1, c2 > 0 oraz n0 >= 0 takie, że
    dla każdego n >= n0:
        c1 * h(n) <= f(n) <= c2 * h(n)

Dowód:
1. Dla dużych n, n + a > 0 (bo a jest stałą).
2. Rozważmy iloraz:
       (n + a)^b / n^b = (1 + a/n)^b
3. Gdy n → ∞, (1 + a/n)^b → 1 (granica z definicji ciągłości).
4. Zatem istnieją stałe c1, c2 > 0 oraz n0 takie, że:
       c1 <= (n + a)^b / n^b <= c2
   dla wszystkich n >= n0.
5. Z definicji Θ wynika:
       (n + a)^b = Θ(n^b)
"""

def shifted_power(n: int, a: float, b: float) -> float:
    """
    Computes (n + a)^b for given n, a, b.
    """
    return (n + a) ** b

def is_theta_equivalent(a: float, b: float, n_values) -> bool:
    """
    Checks if (n + a)^b = Θ(n^b) using the definition of Big Theta.
    This means we need constants c1, c2 > 0 and n0 such that:
        c1 * n^b <= (n + a)^b <= c2 * n^b
    for all n >= n0.
    """
    if b <= 0:
        raise ValueError("b must be positive")

    ratios = []
    for n in n_values:
        if n <= 0:
            continue
        base_val = n ** b
        shifted_val = shifted_power(n, a, b)
        if base_val == 0:
            continue
        ratios.append(shifted_val / base_val)

    if not ratios:
        return False

    c1 = min(ratios)
    c2 = max(ratios)

    return c1 > 0 and c2 < float('inf')

if __name__ == "__main__":
    # Demonstration
    a_demo = 5
    b_demo = 2
    n_values_demo = range(1, 11)
    print(f"Demonstrating (n + {a_demo})^{b_demo} and n^{b_demo}:")
    for n in n_values_demo:
        print(f"n={n:2d} | shifted={(shifted_power(n, a_demo, b_demo)):6.2f} | base={(n**b_demo):6.2f}")

    result = is_theta_equivalent(a_demo, b_demo, range(1, 1000))
    print("\nTheta equivalence holds:", result)
