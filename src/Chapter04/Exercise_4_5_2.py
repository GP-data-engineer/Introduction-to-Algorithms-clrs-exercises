"""
Exercise 4.5-2
Professor Cezar's matrix multiplication algorithm recurrence:
T(n) = aT(n/4) + n²
We find the largest integer 'a' such that the algorithm is asymptotically faster than Strassen's O(n^2.81).
"""

# Polish description:
# Tutaj obliczamy największą wartość parametru a, dla której algorytm Cezara jest szybszy niż Strassena.

import math

def max_a():
    # We need a < 4^(2.81/2) = 4^1.405 ≈ 5.278
    return math.floor(5.278)  # largest integer a = 5

if __name__ == "__main__":
    print("Exercise 4.5-2 Result:")
    print("Largest a:", max_a())
