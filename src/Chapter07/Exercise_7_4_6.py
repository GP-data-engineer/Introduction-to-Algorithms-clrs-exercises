# Exercise_7_4_6.py
# PL: Zadanie 7.4-6 - Modyfikacja PARTITION: losowy wybór 3 elementów i podział względem mediany.
#     Oszacuj prawdopodobieństwo otrzymania w najgorszym przypadku podziału α:(1-α) jako funkcję α.
# EN: Exercise 7.4-6 - Partition modified: pick 3 random elements and partition by their median.
#     Estimate probability that split is as bad as α:(1-α) (worst-case) as function of α.
#
# Implementation:
# - theoretical_probability_bad_split(n, alpha): compute probability that median of 3 has rank <= alpha*n or >= (1-alpha)*n (bad split).
# - simulate_median_of_three(n, alpha, trials): Monte Carlo estimate.
# - Theoretical derivation: pivot must be one of order statistics of sample of size 3; compute prob that median falls in bad rank region.

import random
import math

def theoretical_probability_bad_split(n: int, alpha: float) -> float:
    """
    For distinct elements 1..n, pick 3 distinct ranks uniformly.
    Let r1<r2<r3 be their ranks; pivot is r2 (the median).
    Bad split occurs if r2 <= alpha*n (i.e., median in left alpha fraction) or r2 >= (1-alpha)*n.
    Compute probability exactly by counting all 3-combinations and counting those with median in bad region.
    """
    if not (0 < alpha < 1):
        raise ValueError("alpha must be in (0,1)")
    total = 0
    bad = 0
    # iterate over all triplets of ranks 1..n (combinations without order)
    # For large n this is O(n^3) -> we'll do combinatorial counting:
    # Number of triplets with median = m equals (m-1 choose 1) * (n-m choose 1) = (m-1)*(n-m)
    # So probability median = m is ((m-1)*(n-m)) / C(n,3)
    denom = math.comb(n, 3)
    for m in range(1, n + 1):
        ways_median_m = (m - 1) * (n - m)
        if ways_median_m < 0:
            ways_median_m = 0
        total += ways_median_m
        if m <= math.floor(alpha * n) or m >= math.ceil((1 - alpha) * n):
            bad += ways_median_m
    # total should equal C(n,3)
    # return bad probability
    return bad / denom

def simulate_median_of_three(n: int, alpha: float, trials: int = 20000) -> float:
    random.seed(0)
    count_bad = 0
    for _ in range(trials):
        sample = random.sample(range(1, n + 1), 3)
        sample.sort()
        m = sample[1]
        if m <= alpha * n or m >= (1 - alpha) * n:
            count_bad += 1
    return count_bad / trials

if __name__ == "__main__":
    n = 101
    for alpha in [0.05, 0.1, 0.2]:
        theo = theoretical_probability_bad_split(n, alpha)
        sim = simulate_median_of_three(n, alpha, trials=20000)
        print(f"n={n}, alpha={alpha:.2f} -> theoretical_bad={theo:.4f}, sim={sim:.4f}")
