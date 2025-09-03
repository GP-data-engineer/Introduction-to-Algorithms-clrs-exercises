#!/usr/bin/env python3
# Problem_1_1.py
"""
1-1. Comparison of execution times

For each function f(n) and time t (from the problem statement table),
determine the largest problem size n that can be solved within time t,
assuming the algorithm takes f(n) microseconds to solve a problem of size n.
"""

import math
from typing import Callable, Dict

# Time limits in microseconds
time_limits: Dict[str, int] = {
    "1 second": 1_000_000,
    "1 minute": 60 * 1_000_000,
    "1 hour": 60 * 60 * 1_000_000,
    "1 day": 24 * 60 * 60 * 1_000_000,
    "1 month": 30 * 24 * 60 * 60 * 1_000_000,
    "1 year": 365 * 24 * 60 * 60 * 1_000_000,
    "1 century": 100 * 365 * 24 * 60 * 60 * 1_000_000,
}

# Functions f(n)
functions: Dict[str, Callable[[int], float]] = {
    "log n": lambda n: math.log2(n),
    "sqrt n": lambda n: math.sqrt(n),
    "n": lambda n: n,
    "n log n": lambda n: n * math.log2(n),
    "n^2": lambda n: n ** 2,
    "n^3": lambda n: n ** 3,
    "2^n": lambda n: 2 ** n,
    "n!": lambda n: math.factorial(n),
}

def max_n_for_time(limit_microsec: int, f: Callable[[int], float]) -> int:
    """
    Find the maximum n such that f(n) <= limit (in microseconds).
    Uses exponential search to find an upper bound, then binary search
    to find the exact maximum n.
    """
    # Quick check for n=1
    if f(1) > limit_microsec:
        return 0

    # 1. Exponential search to find an upper bound
    n = 1
    while True:
        try:
            if f(n) > limit_microsec:
                break
            n *= 2
        except OverflowError:
            break

    # 2. Binary search between (n//2, n) to find the exact maximum
    low, high = n // 2, n
    while low < high:
        mid = (low + high) // 2
        try:
            if f(mid) <= limit_microsec:
                low = mid + 1
            else:
                high = mid
        except OverflowError:
            high = mid

    return low - 1

def main():
    header = ["f(n)"] + list(time_limits.keys())
    print("{:<10}".format(header[0]), end="")
    for col in header[1:]:
        print(f"{col:>12}", end="")
    print()

    for name, func in functions.items():
        print(f"{name:<10}", end="")
        for limit in time_limits.values():
            max_n = max_n_for_time(limit, func)
            print(f"{max_n:>12}", end="")
        print()

if __name__ == "__main__":
    main()
