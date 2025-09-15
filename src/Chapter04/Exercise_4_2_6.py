"""
Exercise 4.2-6
Check if splitting kn x kn matrices into n x n blocks can be faster with Strassen.
"""

from math import log2


def compare_direct_vs_block(k: int, n: int, a: float) -> bool:
    """
    Compare direct multiplication vs block multiplication using Strassen.
    Returns True if block method is faster.
    direct_time: time for direct multiplication of (k*n) x (k*n) using Strassen
    block_time: time for multiplying k^2 blocks of size n x n using Strassen
    """
    # Direct multiplication of (k*n) x (k*n)
    direct_time = a * ((k * n) ** (log2(7)))

    # Block multiplication: k^3 multiplications of n x n blocks
    block_time = (k ** 3) * (a * (n ** (log2(7))))

    return block_time < direct_time


if __name__ == "__main__":
    # Example demonstration
    k_val = 2
    n_val = 4
    a_val = 1.0
    result = compare_direct_vs_block(k_val, n_val, a_val)
    print(f"Comparing direct vs block multiplication for k={k_val}, n={n_val}, a={a_val}")
    print(f"Block method faster? {result}")
