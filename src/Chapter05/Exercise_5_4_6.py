"""
Exercise 5.4-6
English: n balls into n bins. Expected number of empty bins, bins with exactly one ball,
and bins with exactly two balls.
Polish: n kul do n urn. Oczekiwana liczba pustych urn, urn z jedną kulą i urn z dwiema kulami.
"""

# Polish description:
# Pusta urna: (1 - 1/n)^n ≈ e^-1, więc oczekiwana liczba ≈ n/e.
# Dokładnie jedna kula: n*(1/n)*(1 - 1/n)^(n-1) ≈ 1/e, więc oczekiwana liczba ≈ n/e.
# Dokładnie dwie kule: (n choose 2)*(1/n^2)*(1 - 2/n)^(n-2) ≈ 1/(2e), więc oczekiwana liczba ≈ n/(2e).

import math

def expected_bins(n: int):
    empty = n * (1 - 1/n)**n
    one = n * (1/n) * (1 - 1/n)**(n-1) * n
    two = n * (math.comb(n, 2) * (1/n**2) * (1 - 2/n)**(n-2))
    return empty, one, two

if __name__ == "__main__":
    print("Exercise 5.4-6 Result:")
    print("Expected bins (empty, one, two) for n=100:", expected_bins(100))
