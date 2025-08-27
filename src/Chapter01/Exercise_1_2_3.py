#!/usr/bin/env python3
# Exercise_1_2_3.py
"""
Find the smallest n such that 100n² < 2ⁿ.
"""

def smallest_n() -> int:
    n = 1
    while 100 * n * n >= (1 << n):
        n += 1
    return n

if __name__ == "__main__":
    result = smallest_n()
    print(f"The smallest n satisfying 100n² < 2ⁿ is {result}.")
