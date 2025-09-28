"""
Exercise 5.1.2
English: Implement RANDOM(a, b) using only RANDOM(0, 1).
Polish: Zaimplementuj RANDOM(a, b) korzystając wyłącznie z RANDOM(0, 1).
"""

# Polish description:
# Funkcja RANDOM(a, b) generuje liczbę całkowitą z przedziału [a, b].
# Używamy RANDOM01() zwracającego 0 lub 1 z równym prawdopodobieństwem.

import random

def RANDOM01():
    return random.choice([0, 1])

def RANDOM(a, b):
    """
    Generate a random integer between a and b using only RANDOM01.
    """
    n = b - a + 1
    bits = n.bit_length()
    while True:
        value = 0
        for _ in range(bits):
            value = (value << 1) | RANDOM01()
        if value < n:
            return a + value

if __name__ == "__main__":
    print("Exercise 5.1.2 Result:")
    samples = [RANDOM(1, 6) for _ in range(10)]
    print("Random samples between 1 and 6:", samples)
