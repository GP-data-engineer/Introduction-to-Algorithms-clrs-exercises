# Exercise 10.3-2 — CLRS
# EN: Implement ALLOCATE-OBJECT and FREE-OBJECT for homogeneous single-table representation.
# PL: Zaimplementuj ALLOCATE-OBJECT i FREE-OBJECT dla homogenicznego zbioru w reprezentacji jednotablicowej.

class MemoryManager:
    def __init__(self, size):
        self.key = [None] * size
        self.next = [None] * size
        self.prev = [None] * size
        self.free = 0
        for i in range(size - 1):
            self.next[i] = i + 1
        self.next[size - 1] = None

    def allocate_object(self):
        if self.free is None:
            raise MemoryError("Brak pamięci")
        x = self.free
        self.free = self.next[x]
        return x

    def free_object(self, x):
        self.next[x] = self.free
        self.free = x

if __name__ == "__main__":
    mm = MemoryManager(5)
    i1 = mm.allocate_object()
    i2 = mm.allocate_object()
    print("Zaalokowano:", i1, i2)
    mm.free_object(i1)
    print("Zwolniono:", i1)
