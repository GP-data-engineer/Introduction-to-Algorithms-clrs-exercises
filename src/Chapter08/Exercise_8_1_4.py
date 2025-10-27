# Exercise_8_1_4.py
# PL:
# Zadanie 8.1-4:
# Niech dany będzie ciąg n elementów do posortowania. Ciąg wejściowy składa się
# z n/k podciągów, po k elementów w każdym. Elementy w każdym podciągu są
# mniejsze niż elementy w następnym podciągu oraz większe od elementów w poprzednim.
# Aby posortować cały ciąg o długości n wystarczy posortować każde k elementów
# we wszystkich n/k podciągach. Wykazać, że dolna granica na liczbę porównań
# w tym wariancie problemu sortowania wynosi Omega(n lg k).
#
# EN:
# Exercise 8.1-4:
# Consider an array of length n consisting of n/k runs (blocks) of k elements each,
# where elements in each block are all smaller than those in the next block,
# so to sort the whole array it suffices to sort each block separately.
# Show the lower bound on number of comparisons is Omega(n log k).
#
# Idea:
# Number of possible permutations consistent with the block-structure = (k!)^(n/k).
# Any comparison-based algorithm must be able to distinguish between those many outcomes,
# so number of leaves >= (k!)^(n/k) -> comparisons >= log2((k!)^(n/k)) = (n/k) log2(k!) = Theta(n log k).

import math

def lower_bound_n_lgk(n: int, k: int) -> float:
    """
    Returns the information-theoretic lower bound on comparisons:
    (n/k) * log2(k!) which is Theta(n log k).
    """
    if n <= 0 or k <= 0:
        raise ValueError("n and k must be positive")
    if n % k != 0:
        raise ValueError("n must be divisible by k for this variant (as stated)")
    # log2(k!) via lgamma
    log2_k_fact = math.lgamma(k + 1) / math.log(2.0)
    return (n // k) * log2_k_fact

def asymptotic_check(n: int, k: int) -> dict:
    """Return numerical illustration comparing lower bound to n*log2(k)."""
    lb = lower_bound_n_lgk(n, k)
    approx_n_lgk = n * math.log2(k)
    return {"lower_bound": lb, "n_log_k": approx_n_lgk, "ratio": lb / approx_n_lgk if approx_n_lgk>0 else float('inf')}

if __name__ == "__main__":
    for (n,k) in [(100, 2), (100, 5), (120, 10)]:
        vals = asymptotic_check(n, k)
        print(f"n={n}, k={k} -> lower_bound (n/k * log2 k!) = {vals['lower_bound']:.3f}, n lg k = {vals['n_log_k']:.3f}, ratio={vals['ratio']:.3f}")
