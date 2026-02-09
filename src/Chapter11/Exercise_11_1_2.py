# Exercise 11.1-2 — CLRS
# EN: Represent a dynamic set using a bit vector; dictionary operations in O(1).
# PL: Reprezentuj zbiór dynamiczny za pomocą wektora bitowego; operacje słownikowe w czasie O(1).

class BitVectorSet:
    def __init__(self, m):
        # Wektor bitowy długości m — 0 oznacza brak elementu, 1 oznacza obecność
        self.m = m
        self.bits = [0] * m

    def insert(self, k):
        # Ustawiamy bit na 1
        if 0 <= k < self.m:
            self.bits[k] = 1

    def delete(self, k):
        # Ustawiamy bit na 0
        if 0 <= k < self.m:
            self.bits[k] = 0

    def search(self, k):
        # Sprawdzamy bit w czasie O(1)
        return 0 <= k < self.m and self.bits[k] == 1

if __name__ == "__main__":
    s = BitVectorSet(8)
    s.insert(3)
    s.insert(5)
    print("Czy 3 należy do zbioru?", s.search(3))
    print("Czy 4 należy do zbioru?", s.search(4))
