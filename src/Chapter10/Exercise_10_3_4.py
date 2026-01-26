# Exercise 10.3-4 — CLRS
# EN: Design ALLOCATE/ FREE to keep list elements in first m positions.
# PL: Zaprojektuj ALLOCATE/ FREE tak, by elementy listy zajmowały pierwsze m pozycji.

class CompactAllocator:
    def __init__(self, size):
        self.stack = list(reversed(range(size)))  # stos wolnych pozycji
        self.memory = [None] * size

    def allocate(self, key):
        if not self.stack:
            raise MemoryError("Brak wolnych pozycji")
        idx = self.stack.pop()
        self.memory[idx] = {"key": key}
        return idx

    def free(self, idx):
        self.memory[idx] = None
        self.stack.append(idx)

if __name__ == "__main__":
    alloc = CompactAllocator(4)
    i1 = alloc.allocate(100)
    i2 = alloc.allocate(200)
    alloc.free(i1)
    print("Zwolniono:", i1)
