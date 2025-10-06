"""
Problem 5-1: Probabilistic Counting

English:
We analyze the probabilistic counter (Morris counter).
(a) Show that the expected value represented on the counter after n INCREMENT operations
    is exactly n.
(b) Analyze the variance of the counter value when n_i = 100^i.

Polish:
Analizujemy licznik probabilistyczny (licznik Morrisa).
(a) Pokaż, że wartość oczekiwana reprezentowana na liczniku po n operacjach INCREMENT
    wynosi dokładnie n.
(b) Oszacuj wariancję wartości na liczniku, gdy n_i = 100^i.
"""

# Polish description:
# (a) Wartość oczekiwana licznika po n operacjach to n (dowód opiera się na liniowości wartości oczekiwanej).
# (b) Dla n_i = 100^i wariancja rośnie szybko, bo skoki wartości są bardzo duże.
#     Przybliżenie: Var ≈ n * (100^2 - 1)/12 (analogia do zmiennej losowej o dużych krokach).

def expected_value_after_n_increments(n: int) -> int:
    """
    (a) Expected value after n increments is exactly n.
    """
    return n

def variance_estimate(n: int) -> float:
    """
    (b) Estimate variance when n_i = 100^i.
    Approximation: variance grows proportionally to n due to large jumps.
    """
    # Przybliżenie: wariancja ~ n * (100^2 - 1)/12
    return n * (100**2 - 1) / 12

if __name__ == "__main__":
    print("Problem 5-1 Results:")
    print("(a) Expected value after 10 increments:", expected_value_after_n_increments(10))
    print("(b) Variance estimate after 10 increments:", variance_estimate(10))
