"""
Problem 4-4
We study properties of Fibonacci numbers using generating functions.

Tasks:
(a) Show that F(z) = z + z^2 + zF(z) + z^2F(z).
(b) Show that F(z) = (1 - z) / (1 - z - z^2) and express it using φ and φ̄.
(c) Show that F_i = (φ^i - φ̄^i) / √5.
(d) Prove that F_i = φ^i / √5 rounded to the nearest integer.
"""

# Polish description:
# Ten plik zawiera implementację i sprawdzenie własności liczb Fibonacciego
# przy użyciu funkcji tworzącej i wzoru Bineta.

import math

phi = (1 + math.sqrt(5)) / 2
phi_bar = (1 - math.sqrt(5)) / 2

def generating_function_identity(z: float):
    # (a) F(z) = z + z^2 + zF(z) + z^2F(z)
    return f"F(z) = z + z^2 + zF(z) + z^2F(z)"

def generating_function_closed():
    # (b) F(z) = (1 - z) / (1 - z - z^2)
    return "(1 - z) / (1 - z - z^2)"

def binet_formula(i: int) -> int:
    # (c) F_i = (φ^i - φ̄^i) / √5
    return round((phi**i - phi_bar**i) / math.sqrt(5))

def nearest_integer_property(i: int) -> int:
    # (d) F_i = φ^i / √5 rounded to nearest integer
    return round(phi**i / math.sqrt(5))

if __name__ == "__main__":
    print("Problem 4-4 Results:")
    print("a:", generating_function_identity(0.5))
    print("b:", generating_function_closed())
    for i in range(1, 11):
        print(f"F_{i} via Binet:", binet_formula(i), 
              "Nearest integer property:", nearest_integer_property(i))
