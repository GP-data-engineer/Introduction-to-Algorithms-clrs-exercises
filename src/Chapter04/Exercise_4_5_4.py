"""
Exercise 4.5-4
Solve recurrence T(n) = 3T(n/2) + n using:
a) Master Theorem
b) Recursion tree
c) Substitution method
d) Find largest r such that T(n) = O(n^r)
"""

# Polish description:
# Rozwiązujemy rekurencję T(n) = 3T(n/2) + n różnymi metodami.
# Wynik: Θ(n^log₂3) ≈ Θ(n^1.585).
# Największe r: r = log₂3.

import math

def master_theorem():
    return "Θ(n^log₂3) ≈ Θ(n^1.585)"

def recursion_tree():
    return "Θ(n^log₂3) ≈ Θ(n^1.585)"

def substitution_method():
    return "Θ(n^log₂3) ≈ Θ(n^1.585)"

def largest_r():
    return math.log(3, 2)  # log₂3 ≈ 1.585

if __name__ == "__main__":
    print("Exercise 4.5-4 Results:")
    print("a) Master Theorem:", master_theorem())
    print("b) Recursion Tree:", recursion_tree())
    print("c) Substitution Method:", substitution_method())
    print("d) Largest r:", largest_r())
