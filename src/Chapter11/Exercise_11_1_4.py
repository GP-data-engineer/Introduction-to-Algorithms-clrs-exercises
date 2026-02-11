# Exercise 11.1-4 — CLRS
# EN: Direct-address dictionary in a huge table without initialization; O(1) SEARCH/INSERT/DELETE and O(1) init.
# PL: Słownik z adresowaniem bezpośrednim w ogromnej tablicy bez inicjalizacji; SEARCH/INSERT/DELETE w O(1) i inicjalizacja w O(1).

class BigDirectDict:
    def __init__(self, m):
        # Duża tablica na klucze/dane (nie inicjalizujemy sensownie całej)
        self.m = m
        self.keys = [None] * m
        self.values = [None] * m
        # Tablica stosu używanych indeksów: stack[0..size-1]
        self.stack = [0] * m
        # Tablica pozycji: pos[i] mówi, na której pozycji w stack leży indeks i (lub śmieci)
        self.pos = [0] * m
        self.size = 0  # liczba faktycznie używanych pozycji

    def _is_valid_index(self, i):
        # Sprawdzamy, czy i jest aktualnie zajęte w słowniku
        if not (0 <= i < self.m):
            return False
        p = self.pos[i]
        return 0 <= p < self.size and self.stack[p] == i

    def search(self, i):
        # Zwracamy (key, value) lub None
        if self._is_valid_index(i):
            return self.keys[i], self.values[i]
        return None

    def insert(self, i, key, value):
        # Wstawiamy element pod indeksem i, jeśli nie był zajęty
        if not (0 <= i < self.m):
            raise ValueError("Indeks poza zakresem")
        if not self._is_valid_index(i):
            # Dodajemy i na stos używanych pozycji
            self.stack[self.size] = i
            self.pos[i] = self.size
            self.size += 1
        self.keys[i] = key
        self.values[i] = value

    def delete(self, i):
        # Usuwamy element spod indeksu i, jeśli istnieje
        if not self._is_valid_index(i):
            return
        p = self.pos[i]
        last_index = self.stack[self.size - 1]
        # Przenosimy ostatni indeks na miejsce usuwanego
        self.stack[p] = last_index
        self.pos[last_index] = p
        self.size -= 1
        # Dane pod i mogą pozostać — i tak nie będzie uznawane za ważne

if __name__ == "__main__":
    d = BigDirectDict(100)
    d.insert(10, "k10", "v10")
    d.insert(20, "k20", "v20")
    print("SEARCH(10):", d.search(10))
    d.delete(10)
    print("SEARCH(10) po usunięciu:", d.search(10))
