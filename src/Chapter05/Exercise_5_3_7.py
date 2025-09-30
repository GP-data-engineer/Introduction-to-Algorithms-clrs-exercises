"""
Exercise 5.3-7
English: Implement RANDOM-SAMPLE(m, n) that generates a random m-subset of {1,...,n}
in O(m) time, without generating a full permutation.
Polish: Zaimplementuj RANDOM-SAMPLE(m, n), które generuje losowy m-elementowy podzbiór {1,...,n}
w czasie O(m), bez tworzenia pełnej permutacji.
"""

# Polish description:
# Algorytm rekurencyjny: losujemy próbkę z n-1 elementów, a następnie decydujemy,
# czy dodać n, czy wylosowany element i. Dzięki temu każdy m-podzbiór ma takie samo prawdopodobieństwo.

import random

def RANDOM_SAMPLE(m, n):
    if m == 0:
        return set()
    S = RANDOM_SAMPLE(m - 1, n - 1)
    i = random.randint(1, n)
    if i in S:
        S.add(n)
    else:
        S.add(i)
    return S

if __name__ == "__main__":
    print("Exercise 5.3-7 Result:")
    print("Random sample of size 3 from {1..10}:", RANDOM_SAMPLE(3, 10))
