# Exercise 11.4-2 — CLRS
# EN: Implement HASH-DELETE and modify HASH-INSERT to handle DELETED markers.
# PL: Zaimplementuj HASH-DELETE i zmodyfikuj HASH-INSERT, aby obsługiwały znacznik DELETED.

DELETED = object()

class HashTableOpen:
    def __init__(self, m):
        self.m = m
        self.T = [None] * m

    def h(self, k, i):
        return (k + i) % self.m

    def insert(self, k):
        for i in range(self.m):
            pos = self.h(k, i)
            if self.T[pos] is None or self.T[pos] is DELETED:
                self.T[pos] = k
                return pos
        raise OverflowError("Hash table overflow")

    def search(self, k):
        for i in range(self.m):
            pos = self.h(k, i)
            if self.T[pos] is None:
                return None
            if self.T[pos] == k:
                return pos
        return None

    def delete(self, k):
        pos = self.search(k)
        if pos is not None:
            self.T[pos] = DELETED

if __name__ == "__main__":
    h = HashTableOpen(11)
    h.insert(10)
    h.insert(21)
    print("Before delete:", h.T)
    h.delete(10)
    print("After delete:", h.T)
