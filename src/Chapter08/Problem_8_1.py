"""
Problem_8_1.py

EN:
Implementation and computational illustrations for Problem 8.1 (CLRS):
"Probabilistic lower bounds on the running time of comparison sorting".
This module provides:
 - factorial_leaves(n): number of leaves = n! and probability 1/n! for each leaf under uniform permutation model
 - lower_bound_log2_factorial(n): log2(n!) lower bound on worst-case comparisons
 - compute_min_external_path_lengths(k): compute d(k) by dynamic programming where
     d(0)=d(1)=0 and d(k)=min_{1<=i<=k-1} ( d(i) + d(k-i) + k )
   which models minimal external path length for decision trees with k leaves
 - demo_dp_values(k_max): show d(k) values and compare to Theta(k log k)
 - randomized_quicksort_count / deterministic_quicksort_count: instrumented quicksorts counting comparisons
 - compare_sorts_on_all_permutations(n): compute average number of comparisons of randomized and deterministic variants over all permutations (for small n)
 - short textual explanations (PL/EN) following CLRS parts (a)-(f).
Note: computational illustrations are for small n only (combinatorial explosion).

PL:
Implementacja i ilustracje obliczeniowe do zadania 8.1 (CLRS):
"Probabilistyczne dolne ograniczenia na czas działania sortowania za pomocą porównań".
Moduł zawiera funkcje:
 - factorial_leaves(n): n! i prawdopodobieństwo 1/n!
 - lower_bound_log2_factorial(n): log2(n!) - dolna granica porównań
 - compute_min_external_path_lengths(k): oblicza d(k) według rekurencji z zadania
 - demo_dp_values(k_max): pokazuje wartości d(k) i porównuje z Theta(k log k)
 - instrumentowane quicksorty liczące porównania (randomized i deterministyczny wariant)
 - compare_sorts_on_all_permutations(n): porównanie średniej liczby porównań dla małych n
 - krótkie opisy (PL/EN) odpowiadające punktom (a)-(f)

Uwaga: niektóre obliczenia (np. wszystkie permutacje) są wykonywalne jedynie dla małych n (np. n <= 8).
"""

from typing import Tuple, List, Dict
import math
import itertools
import random
import statistics

# -------------------------
# (a) Leaves and probabilities
# -------------------------
def factorial_leaves(n: int) -> Tuple[int, float]:
    """
    Return (n!, probability) where probability = 1/n! for each leaf under uniform permutation model.
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    n_fact = math.factorial(n)
    prob = 1.0 / n_fact if n_fact > 0 else 0.0
    return n_fact, prob

# -------------------------
# (e) lower bound via log2(n!)
# -------------------------
def lower_bound_log2_factorial(n: int) -> float:
    """
    Compute log2(n!) using math.lgamma for numerical stability.
    Returns log2(n!) which is the information-theoretic lower bound on comparisons.
    """
    if n <= 1:
        return 0.0
    ln_n_fact = math.lgamma(n + 1)  # ln(n!)
    return ln_n_fact / math.log(2.0)

# -------------------------
# (b)(c)(d) Compute minimal external path length d(k) by DP
# d(0)=d(1)=0
# d(k) = min_{1 <= i <= k-1} ( d(i) + d(k-i) + k )
# This is the recurrence described in CLRS exercise 8.1 parts (b)-(d).
# -------------------------
def compute_min_external_path_lengths(k_max: int) -> List[int]:
    """
    Compute list d[0..k_max] where d[k] is minimal external path length for decision tree with k leaves.
    Uses dynamic programming with O(k_max^2) time.
    """
    if k_max < 0:
        raise ValueError("k_max must be non-negative")
    d = [0] * (k_max + 1)
    # d[0] = 0, d[1] = 0 already
    for k in range(2, k_max + 1):
        best = None
        # try all splits i (number of leaves in left subtree)
        for i in range(1, k // 2 + 1):
            j = k - i
            # symmetry: consider pair (i,j) and (j,i) produce same d(i)+d(j)+k
            val = d[i] + d[j] + k
            if best is None or val < best:
                best = val
        d[k] = best
    return d

def demo_dp_values(k_max: int = 50) -> List[Dict[str, float]]:
    """
    Return summary list of dictionaries for k=1..k_max with fields:
      k, d_k, k_log2_k, ratio = d_k / (k * log2 k)
    This helps illustrate d(k) = Omega(k log k).
    """
    d = compute_min_external_path_lengths(k_max)
    rows = []
    for k in range(1, k_max + 1):
        d_k = d[k] if k < len(d) else None
        if k <= 1:
            k_log = 0.0
        else:
            k_log = k * math.log2(k)
        ratio = (d_k / k_log) if (k_log > 0 and d_k is not None) else float('nan')
        rows.append({"k": k, "d_k": d_k, "k_log2_k": k_log, "ratio": ratio})
    return rows

# -------------------------
# Instrumented quicksorts to count comparisons
# We'll provide:
# - randomized_quicksort_count(A): uses random.choice pivot and counts comparisons
# - deterministic_quicksort_first_pivot_count(A): always uses first element as pivot (deterministic)
# These are used to illustrate (f) by empirical averaging over permutations for small n.
# -------------------------
def lomuto_partition_count(A: List[int], lo: int, hi: int, counters: dict) -> int:
    pivot = A[hi]
    i = lo - 1
    for j in range(lo, hi):
        counters['comparisons'] += 1
        if A[j] <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[hi] = A[hi], A[i+1]
    return i + 1

def randomized_quicksort_count(A: List[int], counters: dict):
    """
    In-place randomized quicksort counting comparisons.
    counters is dict with 'comparisons' key.
    """
    def _qs(lo: int, hi: int):
        if lo < hi:
            # pick random pivot by swapping a random index to hi
            r = random.randint(lo, hi)
            A[r], A[hi] = A[hi], A[r]
            q = lomuto_partition_count(A, lo, hi, counters)
            _qs(lo, q - 1)
            _qs(q + 1, hi)
    _qs(0, len(A) - 1)

def deterministic_quicksort_first_pivot_count(A: List[int], counters: dict):
    """
    Deterministic quicksort always choosing first element as pivot (we swap first to hi).
    """
    def _qs(lo: int, hi: int):
        if lo < hi:
            # move first element to end to use lomuto partition (effectively choosing first)
            A[lo], A[hi] = A[hi], A[lo]
            q = lomuto_partition_count(A, lo, hi, counters)
            _qs(lo, q - 1)
            _qs(q + 1, hi)
    _qs(0, len(A) - 1)

# -------------------------
# (f) Compare randomized vs deterministic averages over all permutations (for small n)
# We'll compute:
#   - expected comparisons of randomized algorithm (by Monte-Carlo) across permutations
#   - exact average for deterministic strategy over *all* permutations (computable by iterating permutations for n up to ~8)
# The function compare_sorts_on_all_permutations returns a dict with numeric summaries.
# -------------------------
def compare_sorts_on_all_permutations(n: int, randomized_trials_per_perm: int = 30, rng_seed: int = 0) -> dict:
    """
    For small n, iterate over all permutations of 0..n-1 and:
     - For deterministic quicksort (first-pivot), compute exact comparisons for each permutation and average.
     - For randomized quicksort, estimate expected comparisons by performing randomized_trials_per_perm runs per permutation and averaging.
    Returns summary dict with averages and lists (if requested).
    Warning: permutations grow as n!, so use n <= 8.
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    if n > 8:
        raise ValueError("n too large for exhaustive permutation enumeration")

    random.seed(rng_seed)
    perms = list(itertools.permutations(range(n)))
    det_counts = []
    rand_avg_counts = []

    for p in perms:
        arr_det = list(p)
        counters_det = {'comparisons': 0}
        # deterministic quicksort on a copy
        a = arr_det.copy()
        deterministic_quicksort_first_pivot_count(a, counters_det)
        det_counts.append(counters_det['comparisons'])

        # randomized: do several runs to estimate expected comparisons for this permutation
        rand_counts_for_perm = []
        for _ in range(randomized_trials_per_perm):
            a2 = list(p)
            counters_rand = {'comparisons': 0}
            randomized_quicksort_count(a2, counters_rand)
            rand_counts_for_perm.append(counters_rand['comparisons'])
        rand_avg_counts.append(statistics.mean(rand_counts_for_perm))

    summary = {
        "n": n,
        "num_permutations": len(perms),
        "det_counts_per_perm": det_counts,
        "rand_avg_counts_per_perm": rand_avg_counts,
        "det_average_over_perms": statistics.mean(det_counts) if det_counts else 0.0,
        "rand_average_over_perms": statistics.mean(rand_avg_counts) if rand_avg_counts else 0.0
    }
    return summary

# -------------------------
# Textual explanations for parts (a)-(f)
# -------------------------
def textual_explanations() -> Dict[str, str]:
    """
    Return textual explanations (EN and PL) for parts (a)-(f) from CLRS exercise 8.1.
    These are compact summaries rather than formal proofs.
    """
    en = {
        "a": "Under uniform random permutation model, there are exactly n! leaves in the decision tree, each reached with probability 1/n!.",
        "b": "Let D(T) be external path length. For a tree with k leaves and left/right subtrees LT/RT with i and k-i leaves respectively, D(T) = D(LT)+D(RT)+k because every leaf depth increases by 1 when attached under root.",
        "c": "Minimize D(T) over shapes yields recurrence d(k)=min_{1<=i<=k-1} ( d(i) + d(k-i) + k ).",
        "d": "The minimum of function i log i + (k-i) log(k-i) occurs near i = k/2, yielding d(k)=Omega(k log k).",
        "e": "For decision tree TA of sorting n elements, D(TA)=Omega(n log2(n!)) = Omega(n log n) and thus expected comparisons Omega(n log n).",
        "f": "Yao's principle (sketch): for any randomized algorithm B there exists a deterministic algorithm A whose expected number of comparisons (under uniform input distribution) is no greater than the expected cost of B. One can show this by averaging over randomness and fixing the random choices that achieve average <= randomized expectation."
    }
    pl = {
        "a": "Dla jednorodnego modelu losowej permutacji mamy dokładnie n! liści drzewa decyzyjnego, każdy osiągany z prawdopodobieństwem 1/n!. ",
        "b": "Jeśli D(T) oznacza zewnętrzną długość ścieżek drzewa, to dla drzewa z korzeniem i poddrzewami LT/RT mamy D(T)=D(LT)+D(RT)+k (ponieważ każdy liść zwiększa swoją głębokość o 1 po dołączeniu).",
        "c": "Minimalizując D(T) otrzymujemy rekurencję d(k)=min_{1<=i<=k-1} ( d(i) + d(k-i) + k ).",
        "d": "Funkcja i lg i + (k-i) lg(k-i) osiąga minimum przy i≈k/2, stąd d(k)=Ω(k lg k).",
        "e": "Dla drzewa decyzyjnego sortowania n elementów D(T_A)=Ω(n lg(n!)) co daje Ω(n lg n) porównań w oczekiwaniu i w najgorszym przypadku.",
        "f": "Zasadniczo, stosując ideę Yao, istnieje deterministyczny algorytm A osiągający oczekiwaną liczbę porównań nie większą niż oczekiwana liczba porównań algorytmu losowego B (patrz CLRS - formalna argumentacja)."
    }
    return {"EN": en, "PL": pl}


# -------------------------
# Main demonstration
# -------------------------
if __name__ == "__main__":
    print("Problem 8.1 (CLRS) computational illustrations\n")

    # (a) factorial leaves
    for n in [0, 1, 3, 5]:
        leaf_count, prob = factorial_leaves(n)
        print(f"(a) n={n}: n! = {leaf_count}, prob(each leaf) = {prob}")

    # (e) lower bound log2(n!)
    for n in [3, 5, 10]:
        lb = lower_bound_log2_factorial(n)
        print(f"(e) n={n}: log2(n!) ≈ {lb:.4f} bits -> lower bound on comparisons")

    # (b)(c)(d) compute d(k) and show growth
    k_max = 30
    rows = demo_dp_values(k_max)
    print("\n(d) Illustrative d(k) and ratio to k log2 k (for k up to 30):")
    for r in rows[1:16]:  # print k=1..15 few values
        print(f"k={r['k']:2d}, d(k)={r['d_k']:6.1f}, k lg k={r['k_log2_k']:7.1f}, ratio={r['ratio']:.4f}")

    # (f) compare randomized vs deterministic averages for n=6 (exhaustive)
    n = 6
    print(f"\n(f) Exhaustive comparison for n={n} permutations (may take a few seconds)...")
    summary = compare_sorts_on_all_permutations(n, randomized_trials_per_perm=10, rng_seed=1)
    print(f"Number permutations: {summary['num_permutations']}")
    print(f"Deterministic (first-pivot) average comparisons over permutations: {summary['det_average_over_perms']:.2f}")
    print(f"Randomized (empirical) average comparisons over permutations: {summary['rand_average_over_perms']:.2f}")
    print("\nTextual summaries (EN / PL):")
    texts = textual_explanations()
    print("EN (short):")
    for k, v in texts['EN'].items():
        print(f" {k}): {v}")
    print("\nPL (sketch):")
    for k, v in texts['PL'].items():
        print(f" {k}): {v}")
