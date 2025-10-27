# Exercise_8_1_3.py
# PL:
# Zadanie 8.1-3: Wykaż, że nie istnieje algorytm sortujący za pomocą porównań, który
# działa w czasie liniowym dla co najmniej połowy spośród n! możliwych danych długości n.
# Czy odpowiedź ulegnie zmianie, jeśli zapytamy o ułamek 1/n, albo 1/2^n, spośród wszystkich danych długości n?
#
# EN:
# Exercise 8.1-3: Show there is no comparison-based sorting algorithm that runs in linear time
# on at least half of all n! inputs. Would the answer change for fraction 1/n or 1/2^n?
#
# Idea:
# Number of different inputs solved within c*n comparisons is at most 2^{c n} (number of leaves at depth <= c n).
# To cover at least half of permutations we need 2^{c n} >= n!/2 -> c >= (log2 n! - 1)/n,
# but log2 n! = Theta(n log n), so c must be Theta(log n) (not constant). Hence impossible.
# For fraction 1/n or 1/2^n, same asymptotic argument: to cover fraction f of n! permutations
# we need 2^{c n} >= f * n! -> log2 n! - log2(1/f) <= c n -> c = Omega(log n).
# So no constant c works for those vanishing fractions either.

import math

def required_c_for_fraction(n: int, fraction: float) -> float:
    """
    For given fraction f (0<f<=1), compute minimal c such that 2^{c n} >= f * n!
    => c >= (log2(n!) + log2(f)) / n  (since log2(f) is negative for f<1).
    Return the RHS value.
    """
    if not (0 < fraction <= 1):
        raise ValueError("fraction must be in (0,1]")
    if n <= 1:
        return 0.0
    log2_n_fact = math.lgamma(n + 1) / math.log(2.0)
    log2_f = math.log2(fraction)
    c = (log2_n_fact + log2_f) / n
    return c

def can_linear_work_for_fraction(n: int, fraction: float, c_linear: float) -> bool:
    """
    Check whether c_linear (a constant factor for linear-time, i.e., c_linear*n comparisons)
    could in principle cover fraction of inputs. Return True if feasible (2^{c n} >= f*n!).
    """
    req = required_c_for_fraction(n, fraction)
    return c_linear >= req

if __name__ == "__main__":
    for n in [10, 50, 200]:
        for frac in [0.5, 1.0/ n, 1.0/(2**n)]:
            req = required_c_for_fraction(n, frac)
            print(f"n={n}, fraction={frac:.5g}, required c >= {req:.4f}")
