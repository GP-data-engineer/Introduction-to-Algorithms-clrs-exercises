# Exercise_8_1_1.py
# PL:
# Zadanie 8.1-1: Jaka jest najmniejsza możliwa głębokość liścia w drzewie decyzyjnym
# odpowiadającym algorytmowi sortującemu za pomocą porównań?
#
# EN:
# Exercise 8.1-1: What is the smallest possible depth of a leaf in the decision tree
# corresponding to a comparison-based sorting algorithm?
#
# Krótkie wyjaśnienie:
# Drzewo decyzyjne dla sortowania ma dokładnie n! liści (po jednym dla każdej permutacji).
# W binarnym drzewie decyzyjnym, wysokość h (maksymalna głębokość liścia) musi spełniać:
# 2^h >= n! => h >= ceil(log2(n!)).
# Zatem minimalna możliwa *maksymalna* głębokość drzewa to >= ceil(log2(n!)), co prowadzi
# do dolnej granicy liczby porównań w najgorszym przypadku: Omega(n log n).
# (Pytanie w CLRS prowadzi do wniosku o log(n!) jako dolnej granicy).
#
# Uwaga: interpretujemy pytanie jako "jak mała może być głębokość liścia w sensie
# najniższa możliwa *maksymalna* głębokość drzewa (height)", bo to jest istotne
# przy wyprowadzaniu dolnej granicy porównań.

import math

def lower_bound_height(n: int) -> int:
    """
    Returns ceil(log2(n!)) — the minimal possible height (maximum leaf depth)
    of a binary decision tree with n! leaves.
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    if n <= 1:
        return 0
    # Use math.lgamma for accurate log factorial: ln(n!) = lgamma(n+1)
    ln_n_fact = math.lgamma(n + 1)
    ln2 = math.log(2.0)
    h = math.ceil(ln_n_fact / ln2)
    return int(h)

def lower_bound_comparisons(n: int) -> float:
    """
    Lower bound on number of comparisons in worst case: log2(n!)
    Return a float value (log2).
    """
    if n <= 1:
        return 0.0
    ln_n_fact = math.lgamma(n + 1)
    return ln_n_fact / math.log(2.0)

if __name__ == "__main__":
    for n in [1, 2, 5, 10, 20]:
        h = lower_bound_height(n)
        lb = lower_bound_comparisons(n)
        print(f"n={n:2d}: ceil(log2(n!)) = {h}, log2(n!) ≈ {lb:.4f}")
