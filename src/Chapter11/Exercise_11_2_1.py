# Exercise 11.2-1 (CLRS)
# PL:
# Załóżmy, że funkcja haszująca odwzorowuje n różnych kluczy w tablicę T długości m.
# Przy prostym równomiernym haszowaniu oblicz oczekiwaną liczbę kolizji,
# tj. oczekiwaną liczbę par (k,l), k≠l, takich że h(k)=h(l).
#
# EN:
# Assume a hash function maps n distinct keys into a table of size m.
# Under simple uniform hashing compute the expected number of collisions,
# i.e. expected number of pairs (k,l), k≠l, such that h(k)=h(l).

def expected_collisions(n: int, m: int) -> float:
    # number of unordered pairs
    pairs = n * (n - 1) / 2
    # probability that two distinct keys collide
    prob_collision = 1 / m
    # expected value
    return pairs * prob_collision


if __name__ == "__main__":
    n = 10
    m = 5
    print("Expected collisions:", expected_collisions(n, m))
