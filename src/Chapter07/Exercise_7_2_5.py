# Exercise_7_2_5.py
# PL: Zadanie 7.2-5 - Zakładamy, że podziały na każdym poziomie algorytmu quicksort są w stosunku 1-alpha do alpha.
#     Pokaż, że najmniejsza głębokość liścia ~ -lg n / lg alpha, a największa ~ -lg n / lg(1-alpha).
# EN: Exercise 7.2-5 - If partitions are (1-alpha):alpha each level, show min leaf depth ~ -lg n / lg alpha and max ~ -lg n / lg(1-alpha).
#
# Implementation:
# - formulas_depths(n, alpha): returns theoretical depths.
# - simulate_depths(n, alpha): simulate recursion sizes until size <=1 to compute actual integer depths for min & max path.

import math
from typing import Tuple

def formulas_depths(n: int, alpha: float) -> Tuple[float, float]:
    """
    Return (min_depth, max_depth) as real valued approximations:
    min_depth ≈ -log(n)/log(alpha)
    max_depth ≈ -log(n)/log(1-alpha)
    """
    if not (0 < alpha <= 0.5):
        raise ValueError("alpha must satisfy 0 < alpha <= 1/2")
    min_depth = -math.log(n, alpha)  # -lg n / lg alpha
    max_depth = -math.log(n, 1 - alpha)
    return min_depth, max_depth

def simulate_depths(n: int, alpha: float) -> Tuple[int, int]:
    """
    Simulate repeated multiplication by alpha (small branch) and by (1-alpha) (big branch)
    until size <= 1, counts integer depth (ceil).
    """
    if n <= 1:
        return 0, 0
    # min depth: repeatedly multiply by alpha (smallest child) until <=1
    depth_min = 0
    size = n
    while size > 1:
        size = size * alpha
        depth_min += 1
    # max depth: repeatedly multiply by (1-alpha)
    depth_max = 0
    size = n
    while size > 1:
        size = size * (1 - alpha)
        depth_max += 1
    return depth_min, depth_max

if __name__ == "__main__":
    n = 1024
    for alpha in [0.1, 0.2, 0.3]:
        fmin, fmax = formulas_depths(n, alpha)
        smin, smax = simulate_depths(n, alpha)
        print(f"n={n}, alpha={alpha:.2f} -> formula_min={fmin:.3f}, sim_min={smin}; formula_max={fmax:.3f}, sim_max={smax}")
