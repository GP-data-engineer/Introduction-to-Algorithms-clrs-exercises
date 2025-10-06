"""
Exercise 6.1-2
English: Show that an n-element heap has height floor(log n).
Polish: Pokaż, że n-elementowy kopiec ma wysokość ⌊lg n⌋.
"""

import math

def heap_height(n: int):
    return math.floor(math.log2(n))

if __name__ == "__main__":
    print("Exercise 6.1-2 Result:")
    print("Height for n=10:", heap_height(10))
