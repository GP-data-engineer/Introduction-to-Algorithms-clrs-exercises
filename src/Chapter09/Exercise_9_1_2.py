# Exercise 9.1-2 — CLRS
# Znajdowanie minimum i maksimum w pesymistycznym przypadku
# Find both minimum and maximum using ⌊3n/2⌋ - 2 comparisons

def znajdz_min_max(tablica):
    n = len(tablica)
    if n == 0:
        raise ValueError("Tablica nie może być pusta")

    if n % 2 == 0:
        if tablica[0] < tablica[1]:
            minimum, maksimum = tablica[0], tablica[1]
        else:
            minimum, maksimum = tablica[1], tablica[0]
        start = 2
    else:
        minimum = maksimum = tablica[0]
        start = 1

    # Porównujemy parami
    for i in range(start, n, 2):
        if i + 1 >= n:
            if tablica[i] < minimum:
                minimum = tablica[i]
            if tablica[i] > maksimum:
                maksimum = tablica[i]
        else:
            if tablica[i] < tablica[i + 1]:
                min_kand, max_kand = tablica[i], tablica[i + 1]
            else:
                min_kand, max_kand = tablica[i + 1], tablica[i]
            if min_kand < minimum:
                minimum = min_kand
            if max_kand > maksimum:
                maksimum = max_kand

    return (minimum, maksimum)

if __name__ == "__main__":
    dane = [5, 3, 8, 2, 7, 1, 4]
    wynik = znajdz_min_max(dane)
    print("Minimum:", wynik[0], "Maksimum:", wynik[1])
