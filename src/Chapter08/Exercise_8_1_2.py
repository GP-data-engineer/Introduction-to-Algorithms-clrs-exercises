# Exercise_8_1_2.py
# PL:
# Zadanie 8.1-2: Wyprowadź dokładne oszacowanie asymptotyczne na lg(n!) bez korzystania
# ze wzoru Stirlinga. Oblicz w tym celu sumę sum_{k=1..n} lg k, stosując metody z dodatku.
#
# EN:
# Exercise 8.1-2: Derive asymptotic estimate for lg(n!) without using Stirling.
# Compute sum_{k=1..n} lg k and show it is Theta(n log n).
#
# Implementacja:
# - direct_sum_log2(n): oblicza dokładnie sumę log2(k) dla k=1..n (bez Stirlinga),
# - approx_stirling(n): porównanie z przybliżeniem Stirlinga (dla porównania),
# - show_asymptotic(n): zwraca wartości pomocnicze ilustrujące n lg n - n ln e + Theta(log n).
#
# Uwaga: w kodzie używamy sumy logów (sum log2 k) aby wyprowadzić asymptotykę.

import math

def direct_sum_log2(n: int) -> float:
    """Compute lg(n!) = sum_{k=1..n} log2(k) directly (sum of logs base 2)."""
    if n <= 1:
        return 0.0
    s = 0.0
    for k in range(1, n+1):
        s += math.log2(k)
    return s

def approx_via_integral(n: int) -> float:
    """
    Use integral approximation: sum_{k=1..n} log2(k) ≈ integral_1^n log2 x dx + O(log n)
    integral_1^n log2 x dx = (n+1)log2(n+1) - (n+1)/ln 2 + const (up to O(1))
    We'll return n*log2(n) - n/log(2) (which is n lg n - n lg e) as main terms.
    """
    if n <= 1:
        return 0.0
    return n * math.log2(n) - (n / math.log(2.0))  # main terms (units mix but illustrative)

def approx_stirling(n: int) -> float:
    """
    Return Stirling approximation for log2(n!):
    log2(n!) ≈ (n + 0.5) log2 n - n log2 e + 0.5 log2(2*pi)  (base 2)
    We include the 0.5 log term to show the Theta(log n) remainder.
    """
    if n <= 1:
        return 0.0
    return (n + 0.5) * math.log2(n) - n * math.log2(math.e) + 0.5 * math.log2(2 * math.pi)

if __name__ == "__main__":
    for n in [5, 10, 100, 1000]:
        exact = direct_sum_log2(n)
        approx_int = approx_via_integral(n)
        approx_st = approx_stirling(n)
        print(f"n={n:4d}: exact lg(n!)={exact:.6f}, integral approx ≈ {approx_int:.6f}, stirling ≈ {approx_st:.6f}")
