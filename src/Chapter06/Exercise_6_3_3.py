"""
Exercise 6.3-3
English: Show that in an n-element heap there are at most ceil(n/2^(h+1)) nodes of height h.
Polish: Pokaż, że w n-elementowym kopcu jest co najwyżej ⌈n/2^(h+1)⌉ węzłów o wysokości h.
"""

import math

# Polish description:
# Liczba węzłów na wysokości h maleje wykładniczo.
# Wysokość h oznacza odległość od liści, więc liczba węzłów ≤ ⌈n / 2^(h+1)⌉.

def nodes_at_height(n: int, h: int):
    return math.ceil(n / (2**(h+1)))

if __name__ == "__main__":
    print("Exercise 6.3-3 Result:")
    print("Nodes at height h=1 for n=16:", nodes_at_height(16, 1))
