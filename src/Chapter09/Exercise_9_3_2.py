# Exercise 9.3-2 (EN): Show that for n > 140, SELECT guarantees at least ⌈n/4⌉ elements > and < median of medians.
# Exercise 9.3-2 (PL): Pokaż, że dla n > 140 SELECT gwarantuje co najmniej ⌈n/4⌉ elementów większych i mniejszych od mediany median.

import math

def lower_bound_partition(n):
    """
    Oblicza dolną granicę liczby elementów większych/mniejszych od mediany median.
    """
    if n <= 140:
        return None
    return math.ceil(n / 4)

if __name__ == "__main__":
    n = 200
    bound = lower_bound_partition(n)
    print(f"Dla n = {n}, co najmniej ⌈n/4⌉ = {bound} elementów większych/mniejszych od mediany median.")
