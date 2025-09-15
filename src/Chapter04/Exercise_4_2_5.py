"""
Exercise 4.2-5
Show that multiplying 2n x 2n matrices with Strassen takes 7M(n) + c*n^2 time.
"""

def time_for_2n(Mn: float, n: int, c: float) -> float:
    """Compute time for 2n x 2n multiplication."""
    return 7 * Mn + c * (n ** 2)


def verify_strassen_time(a: float, n: int) -> float:
    """Verify that if M(n) = a * n^(log2(7)), then time matches a*(2n)^(log2(7))."""
    from math import log2
    return a * ((2 * n) ** (log2(7)))


if __name__ == "__main__":
    print("Time for 2n x 2n:", time_for_2n(100, 4, 2))
    print("Verification:", verify_strassen_time(1, 4))
