"""
Explanation (in Polish):

1. C_{XY} * 2^{n+1} = O(2^n) — prawda, bo 2^{n+1} = 2 * 2^n, a stała nie zmienia klasy złożoności.
2. C_{XY} * 2^n = O(2^{2^n}) — prawda, bo 2^{2^n} rośnie znacznie szybciej niż 2^n.

Poprawiona implementacja sprawdzania Big-O uwzględnia trend ilorazu, aby uniknąć fałszywych wyników.
"""

def is_big_o_of(expr_func, bound_func, n_values, tolerance=1e6):
    """
    Empirically checks if expr_func(n) = O(bound_func(n)).
    Conditions:
    1. Ratio expr/bound must stay below tolerance.
    2. Ratio should not grow drastically (trend check).
    """
    ratios = []
    for n in n_values:
        bound_val = bound_func(n)
        if bound_val == 0:
            continue
        ratios.append(expr_func(n) / bound_val)

    if not ratios:
        return False

    # Warunek 1: ograniczenie górne
    if max(ratios) >= tolerance:
        return False

    # Warunek 2: brak silnego trendu wzrostowego
    if ratios[-1] > ratios[0] * 10:  # wzrost >10x w badanym zakresie
        return False

    return True

# Example functions for the given problem
def expr1(n, C=1):
    return C * (2 ** (n + 1))

def bound1(n):
    return 2 ** n

def expr2(n, C=1):
    return C * (2 ** n)

def bound2(n):
    return 2 ** (2 ** n)

if __name__ == "__main__":
    n_values_demo = range(1, 20)
    print("Check if C*2^(n+1) = O(2^n):", is_big_o_of(lambda n: expr1(n, 3), bound1, n_values_demo))
    print("Check if C*2^n = O(2^(2^n)):", is_big_o_of(lambda n: expr2(n, 5), bound2, n_values_demo))
