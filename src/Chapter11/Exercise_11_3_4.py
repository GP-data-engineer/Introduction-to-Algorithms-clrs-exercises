# Exercise 11.2-4 — CLRS
# EN: Memory allocation inside hash table using free list.
# PL: Przydzielanie i zwalnianie pamięci w tablicy haszującej z listą wolnych pozycji.

class FreeListHashTable:
    def __init__(self, m):
        self.m = m
        self.table = [None] * m
        self.free = list(range(m))  # lista wolnych pozycji

    def allocate(self, key):
        if not self.free:
            raise MemoryError("Brak wolnych pozycji")
        idx = self.free.pop()
        self.table[idx] = key
        return idx

    def free_object(self, idx):
        self.table[idx] = None
        self.free.append(idx)

if __name__ == "__main__":
    ht = FreeListHashTable(5)
    i1 = ht.allocate("A")
    i2 = ht.allocate("B")
    print("Tablica:", ht.table)
    ht.free_object(i1)
    print("Po zwolnieniu:", ht.table)
