# Exercise 9.1-1 — CLRS
# Znajdowanie drugiej najmniejszej liczby w pesymistycznym przypadku
# Find the second smallest number using n + ⌊lg n⌋ - 2 comparisons

import math

def znajdz_druga_najmniejsza(tablica):
    # Tworzymy drzewo turniejowe, gdzie każdy element przegrywa tylko z mniejszym
    n = len(tablica)
    if n < 2:
        raise ValueError("Potrzebne są co najmniej dwie liczby")

    # Budujemy drzewo zwycięzców
    drzewo = [[] for _ in range(n)]
    indeksy = list(range(n))

    while len(indeksy) > 1:
        nowa_runda = []
        for i in range(0, len(indeksy) - 1, 2):
            a, b = indeksy[i], indeksy[i + 1]
            if tablica[a] < tablica[b]:
                drzewo[a].append(tablica[b])
                nowa_runda.append(a)
            else:
                drzewo[b].append(tablica[a])
                nowa_runda.append(b)
        if len(indeksy) % 2 == 1:
            nowa_runda.append(indeksy[-1])
        indeksy = nowa_runda

    # Zwycięzca to najmniejszy element
    zwyciezca = indeksy[0]
    # Druga najmniejsza to najmniejsza z przegranych z najmniejszym
    druga_najmniejsza = min(drzewo[zwyciezca])
    return druga_najmniejsza

if __name__ == "__main__":
    dane = [5, 3, 8, 2, 7, 1, 4]
    wynik = znajdz_druga_najmniejsza(dane)
    print("Druga najmniejsza liczba to:", wynik)
