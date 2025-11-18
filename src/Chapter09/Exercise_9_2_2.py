# Exercise 9.2-2 — CLRS
# EN: Justify that the indicator random variable X and the quantity T(max(k - 1, n - k)) are independent.
# PL: Uzasadnij, że wskaźnikowa zmienna losowa X i wielkość T(max(k - 1, n - k)) są niezależne.

import random

def randomized_select_trace(tablica, p, r, i, log=None):
    # Rekurencyjny wybór i-tego najmniejszego elementu z logowaniem
    if log is None:
        log = []

    if p == r:
        log.append(("X", p, r))
        return tablica[p], log

    q = randomized_partition(tablica, p, r)
    k = q - p + 1
    log.append(("X", p, r))  # Zmienna wskaźnikowa X — czy trafiliśmy w pozycję?

    if i == k:
        return tablica[q], log
    elif i < k:
        return randomized_select_trace(tablica, p, q - 1, i, log)
    else:
        return randomized_select_trace(tablica, q + 1, r, i - k, log)

def partition(tablica, p, r):
    x = tablica[r]
    i = p - 1
    for j in range(p, r):
        if tablica[j] <= x:
            i += 1
            tablica[i], tablica[j] = tablica[j], tablica[i]
    tablica[i + 1], tablica[r] = tablica[r], tablica[i + 1]
    return i + 1

def randomized_partition(tablica, p, r):
    i = random.randint(p, r)
    tablica[r], tablica[i] = tablica[i], tablica[r]
    return partition(tablica, p, r)

def T(n):
    # Symulacja czasu działania T(n)
    return n  # uproszczona wersja: T(n) = n

def simulate_independence(tablica, i):
    # Symulacja niezależności X i T(max(k-1, n-k))
    wynik, log = randomized_select_trace(tablica.copy(), 0, len(tablica) - 1, i)
    ostatni = log[-1]
    p, r = ostatni[1], ostatni[2]
    k = i
    n = len(tablica)
    t_wartosc = T(max(k - 1, n - k))
    return {
        "X": ostatni,
        "T(max(k-1, n-k))": t_wartosc,
        "wynik": wynik
    }

if __name__ == "__main__":
    dane = [9, 3, 7, 1, 5, 2, 6, 8, 4]
    i = 5
    wynik = simulate_independence(dane, i)
    print("Symulacja niezależności:")
    print(wynik)
