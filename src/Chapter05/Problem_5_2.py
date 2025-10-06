"""
Problem 5-2: Searching in an Unsorted Array

English:
We analyze three algorithms for searching a value x in an unsorted array A of length n:
(a) RANDOM-SEARCH: pick random indices until x is found.
(b) DETERMINISTIC-SEARCH: scan array sequentially until x is found.
(c) SCRAMBLE-SEARCH: randomly permute array, then do linear search.

We compute expected and worst-case running times.

Polish:
Analizujemy trzy algorytmy wyszukiwania wartości x w nieposortowanej tablicy A o długości n:
(a) RANDOM-SEARCH: losowe indeksy aż do znalezienia x.
(b) DETERMINISTIC-SEARCH: liniowe przeszukiwanie od początku.
(c) SCRAMBLE-SEARCH: losowa permutacja, potem liniowe przeszukiwanie.

Obliczamy oczekiwany i pesymistyczny czas działania.
"""

import random

def random_search(A, x):
    """Randomly search until x is found. Returns number of iterations."""
    n = len(A)
    count = 0
    while True:
        count += 1
        i = random.randint(0, n-1)
        if A[i] == x:
            return count

def deterministic_search(A, x):
    """Sequential search until x is found. Returns index or -1."""
    for i, val in enumerate(A):
        if val == x:
            return i
    return -1

def scramble_search(A, x):
    """Randomly permute array, then do linear search. Returns index or -1."""
    B = A[:]
    random.shuffle(B)
    for i, val in enumerate(B):
        if val == x:
            return i
    return -1

def expected_random_search(n):
    """Expected iterations for RANDOM-SEARCH with one occurrence of x."""
    return n

def worst_random_search(n):
    """Worst-case iterations for RANDOM-SEARCH."""
    return n

def expected_deterministic_search(n):
    """Expected iterations for DETERMINISTIC-SEARCH with random position of x."""
    return (n + 1) / 2

def worst_deterministic_search(n):
    """Worst-case iterations for DETERMINISTIC-SEARCH."""
    return n

def expected_scramble_search(n, k):
    """
    Expected iterations for SCRAMBLE-SEARCH.
    If k=1, expected ~ (n+1)/2.
    If k=0, must scan all n.
    """
    if k == 0:
        return n
    return (n + 1) / (k + 1)

def worst_scramble_search(n, k):
    """Worst-case iterations for SCRAMBLE-SEARCH."""
    return n

if __name__ == "__main__":
    A = [1, 2, 3, 4, 5]
    x = 3
    print("Problem 5-2 Results:")
    print("Random-Search expected iterations (n=5):", expected_random_search(len(A)))
    print("Deterministic-Search expected iterations (n=5):", expected_deterministic_search(len(A)))
    print("Scramble-Search expected iterations (n=5, k=1):", expected_scramble_search(len(A), 1))
