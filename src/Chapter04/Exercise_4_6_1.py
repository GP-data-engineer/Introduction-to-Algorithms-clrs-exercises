"""
Exercise 4.6-1
Provide a simple exact expression for n_j defined by formula (4.27)
in the case where b is a positive integer.
"""

# Polish description:
# Wzór (4.27) definiuje n_j = n / b^j. Jeśli b jest całkowite, to n_j = n / b^j
# jest prostym wyrażeniem. Zwracamy tę postać jako string.

def n_j(n: int, b: int, j: int) -> int:
    # Compute n_j = n / b^j
    return n // (b ** j)

if __name__ == "__main__":
    print("Exercise 4.6-1 Result:")
    print("Example: n=64, b=2, j=3 ->", n_j(64, 2, 3))
