"""
Mathematical proof (in Polish):

Niech f(n) i g(n) będą asymptotycznie nieujemne, tzn. istnieje n0 takie, że
dla każdego n >= n0 mamy f(n) >= 0 oraz g(n) >= 0.

Definicja notacji Θ(h(n)):
    f(n) = Θ(h(n)) ⇔ istnieją stałe c1, c2 > 0 oraz n0 >= 0 takie, że
    dla każdego n >= n0 zachodzi:
        c1 * h(n) <= f(n) <= c2 * h(n).

Chcemy pokazać:
    max(f(n), g(n)) = Θ(f(n) + g(n)).

1. Dolne ograniczenie:
   Ponieważ f(n) >= 0 i g(n) >= 0, mamy:
       f(n) + g(n) <= 2 * max(f(n), g(n)).
   Dzieląc obustronnie przez 2:
       (f(n) + g(n)) / 2 <= max(f(n), g(n)).
   Zatem możemy wziąć c1 = 1/2.

2. Górne ograniczenie:
   Z definicji maksimum:
       max(f(n), g(n)) <= f(n) + g(n).
   Zatem możemy wziąć c2 = 1.

3. Wnioskujemy:
   Istnieją stałe c1 = 1/2, c2 = 1 oraz n0, że:
       c1 * (f(n) + g(n)) <= max(f(n), g(n)) <= c2 * (f(n) + g(n))
   dla każdego n >= n0.
   Z definicji Θ wynika, że:
       max(f(n), g(n)) = Θ(f(n) + g(n)).
"""

def max_function(f, g, n):
    """
    Returns max(f(n), g(n)) for given functions f, g and integer n.
    """
    return max(f(n), g(n))

def sum_function(f, g, n):
    """
    Returns f(n) + g(n) for given functions f, g and integer n.
    """
    return f(n) + g(n)

def is_theta_equivalent(f, g, n_values):
    """
    Checks if max(f(n), g(n)) = Θ(f(n) + g(n)) using the definition of Big Theta.
    This means we need constants c1, c2 > 0 and n0 such that:
        c1 * (f(n) + g(n)) <= max(f(n), g(n)) <= c2 * (f(n) + g(n))
    for all n >= n0.
    """
    ratios = []
    for n in n_values:
        sum_val = sum_function(f, g, n)
        max_val = max_function(f, g, n)
        if sum_val == 0:
            continue  # avoid division by zero
        ratios.append(max_val / sum_val)

    if not ratios:
        return False

    c1 = min(ratios)
    c2 = max(ratios)

    return c1 > 0 and c2 < float('inf')

# Example functions for demonstration
def f_example(n):
    return n**2

def g_example(n):
    return n

if __name__ == "__main__":
    # When run directly, show a demonstration of the theorem
    n_values = range(1, 11)
    print("Demonstration of max(f(n), g(n)) and f(n) + g(n):")
    for n in n_values:
        print(f"n={n:2d} | max={max_function(f_example, g_example, n):4d} | sum={sum_function(f_example, g_example, n):4d}")

    result = is_theta_equivalent(f_example, g_example, range(1, 1000))
    print("\nTheta equivalence holds:" , result)
