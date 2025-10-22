# Exercise_7_4_3.py
# PL: Zadanie 7.4-3 - Pokaż, że wyrażenie q^2 + (n-q-1)^2 osiąga maksimum dla q=0 lub q=n-1.
# EN: Exercise 7.4-3 - Show q^2 + (n-q-1)^2 is maximized at q=0 or q=n-1 for q=0..n-1.
#
# Implementation:
# - simple function that computes the quadratic for q in range and returns argmax.
# - include a small proof note in docstring and demonstrate numerically.

from typing import Tuple

def argmax_quadratic(n: int) -> Tuple[int, int, list]:
    """
    Compute values v(q) = q^2 + (n-q-1)^2 for q=0..n-1,
    return (argmax_q, max_value, values_list).
    """
    values = []
    best_q = 0
    best_val = -1
    for q in range(0, n):
        v = q * q + (n - q - 1) * (n - q - 1)
        values.append(v)
        if v > best_val:
            best_val = v
            best_q = q
    return best_q, best_val, values

if __name__ == "__main__":
    for n in [5, 10, 11]:
        q, val, vals = argmax_quadratic(n)
        print(f"n={n}: argmax q={q}, max={val}, expected q in {{0,{n-1}}}")
