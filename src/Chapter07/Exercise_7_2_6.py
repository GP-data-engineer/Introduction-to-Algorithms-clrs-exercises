# Exercise_7_2_6.py
# PL: Zadanie 7.2-6 - Pokaż, że dla stałego 0 < alpha <= 1/2 prawdopodobieństwo,
#     że dla dowolnej tablicy wejściowej procedura PARTITION utworzy podział bardziej zrównoważony niż 1-alpha do alpha wynosi około 1 - 2alpha.
# EN: Exercise 7.2-6 - Show that probability partition is more balanced than (1-alpha):alpha is about 1 - 2*alpha.
#
# Implementation:
# - theoretical_probability(n, alpha): exact discrete probability that a uniformly random pivot yields split inside (alpha,1-alpha)
# - simulate_probability(n, alpha, trials): Monte Carlo estimate for random arrays/pivots.

import random
from typing import Tuple

def theoretical_probability(n: int, alpha: float) -> float:
    """
    For array of n distinct elements and pivot chosen uniformly at random,
    the pivot must be one of the order statistics with rank in [alpha*n, (1-alpha)*n].
    We compute discrete count of 'good' pivot ranks divided by n.
    """
    if not (0 <= alpha <= 0.5):
        raise ValueError("alpha must satisfy 0 <= alpha <= 0.5")
    # Accept ranks r such that alpha*n <= r-1 <= (1-alpha)*n - 1  (0-based)
    # Simpler: acceptable ranks (1-based) from floor(alpha*n)+1 to ceil((1-alpha)*n)
    low = int(math.floor(alpha * n)) + 1
    high = int(math.ceil((1 - alpha) * n))
    if high < low:
        return 0.0
    good = max(0, high - low + 1)
    return good / n

import math
def simulate_probability(n: int, alpha: float, trials: int = 10000) -> float:
    """
    Monte Carlo: pick random pivot rank uniformly (equivalent) and estimate probability.
    """
    count = 0
    for _ in range(trials):
        # pick pivot rank uniformly from 1..n
        r = random.randint(1, n)
        # check if pivot rank is in acceptable interval
        if alpha * n < r <= (1 - alpha) * n:
            count += 1
    return count / trials

if __name__ == "__main__":
    random.seed(0)
    n = 101
    for alpha in [0.05, 0.1, 0.2]:
        theo = theoretical_probability(n, alpha)
        sim = simulate_probability(n, alpha, trials=20000)
        print(f"n={n}, alpha={alpha:.2f} -> theoretical={theo:.4f}, sim={sim:.4f}, approx 1-2*alpha={1-2*alpha:.4f}")
