"""
Exercise 7.3-2 (CLRS, 4th Edition)
----------------------------------
Pytanie:
Ile wywołań generatora liczb losowych RANDOM jest wykonywanych podczas działania
procedury RANDOMIZED-QUICKSORT w przypadku pesymistycznym i w przypadku optymistycznym?
Podaj odpowiedź z użyciem notacji Θ.

Rozwiązanie:
Każde wywołanie RANDOMIZED-QUICKSORT(n) dokonuje jednego losowania pivotu.
Zatem liczba wywołań generatora RANDOM odpowiada liczbie wywołań funkcji
RANDOMIZED-PARTITION, czyli liczbie wywołań rekurencji.

Niezależnie od przebiegu, pivot losowany jest raz na każde wywołanie rekurencyjne.
Liczba wywołań rekurencyjnych = liczba elementów (n).

W obu przypadkach — pesymistycznym i optymistycznym — pivot losowany jest n razy.

Odpowiedź:
Θ(n)
"""

import random

def randomized_quicksort(arr, counter=None):
    if counter is None:
        counter = {'random_calls': 0}
    if len(arr) <= 1:
        return arr
    counter['random_calls'] += 1
    pivot = random.choice(arr)
    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return randomized_quicksort(left, counter) + mid + randomized_quicksort(right, counter)


def random_call_count(n: int) -> int:
    """Zwraca liczbę wywołań RANDOM dla tablicy długości n."""
    import random
    random.seed(0)
    counter = {'random_calls': 0}
    randomized_quicksort(list(range(n)), counter)
    return counter['random_calls']


if __name__ == "__main__":
    for n in [1, 5, 10, 50]:
        print(f"n={n}, liczba wywołań RANDOM ≈ {random_call_count(n)} (Θ(n))")
