"""
Exercise 4.2-4
Theoretical computation for k in 3x3 multiplication to beat Strassen's complexity.
"""

def compute_k_threshold() -> int:
    """
    Returns the largest k such that multiplying 3x3 matrices with k multiplications
    yields complexity o(n^(log2(7))).
    """
    from math import log2
    # We want k^(log_3(n)) < n^(log2(7))
    # This is a placeholder for demonstration
    return 21  # Example value for demonstration


if __name__ == "__main__":
    print("Largest k for improved complexity:", compute_k_threshold())
