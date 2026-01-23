# Exercise 10.3-2 — CLRS
# EN: Implement ALLOCATE-OBJECT and FREE-OBJECT for homogeneous single-table representation.
# PL: Zaimplementuj ALLOCATE-OBJECT i FREE-OBJECT dla jednotablicowej reprezentacji homogenicznej.

class ObjectPool:
    def __init__(self, size):
        self.pool = [None] * size
        self.free = list(range(size))  # stos wolnych pozycji

    def allocate_object(self, key):
        if not self.free:
            raise MemoryError("Brak wolnych pozycji")
        index = self.free.pop()
        self.pool[index] = {"key": key, "prev": None, "next": None}
        return index

    def free_object(self, index):
        self.pool[index] = None
        self.free.append(index)

if __name__ == "__main__":
    pool = ObjectPool(5)
    idx = pool.allocate_object(42)
    print("Zaalokowano obiekt na pozycji:", idx)
    pool.free_object(idx)
    print("Zwolniono pozycję:", idx)
