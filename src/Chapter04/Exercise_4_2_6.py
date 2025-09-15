"""
Exercise 4.2-6
Check if splitting kn x kn matrices into n x n blocks can be faster with Strassen.
"""

from math import log2

def compare_direct_vs_block(k: int, n: int, a: float) -> bool:
    """
    Compare direct multiplication vs block multiplication using Strassen.
    Returns True if block method is faster.
    Assumes block multiplication can be parallelized, so only k^2 block multiplications are needed in time model.
    """
    direct_time = a * ((k * n) ** (log2(7)))
    block_time = (k ** 2) * (a * (n ** (log2(7))))
    return block_time < direct_time


if __name__ == "__main__":
    k_val = 2
    n_val = 16
    a_val = 1.0
    result = compare_direct_vs_block(k_val, n_val, a_val)
    print(f"Comparing direct vs block multiplication for k={k_val}, n={n_val}, a={a_val}")
    print(f"Block method faster? {result}")

