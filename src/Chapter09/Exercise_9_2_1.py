# Exercise 9.2-1 — CLRS
# EN: Prove that RANDOMIZED-SELECT never makes a recursive call on an array of length 0.
# PL: Udowodnij, że RANDOMIZED-SELECT nigdy nie wywołuje rekurencji dla tablicy długości 0.

import random

def partition(tablica, p, r):
    # Wybór pivota i podział tablicy
    x = tablica[r]
    i = p - 1
    for j in range(p, r):
        if tablica[j] <= x:
            i += 1
            tablica[i], tablica[j] = tablica[j], tablica[i]
    tablica[i + 1], tablica[r] = tablica[r], tablica[i + 1]
    return i + 1

def randomized_partition(tablica, p, r):
    # Losowy wybór pivota
    i = random.randint(p, r)
    tablica[r], tablica[i] = tablica[i], tablica[r]
    return partition(tablica, p, r)

def randomized_select(tablica, p, r, i):
    # Rekurencyjny wybór i-tego najmniejszego elementu
    if p == r:
        return tablica[p]
    q = randomized_partition(tablica, p, r)
    k = q - p + 1
    if i == k:
        return tablica[q]
    elif i < k:
        return randomized_select(tablica, p, q - 1, i)
    else:
        return randomized_select(tablica, q + 1, r, i - k)

if __name__ == "__main__":
    # Przykład działania
    dane = [7, 2, 1, 6, 8, 5, 3, 4]
    i = 4
    wynik = randomized_select(dane, 0, len(dane) - 1, i)
    print(f"{i}-ty najmniejszy element to: {wynik}")
