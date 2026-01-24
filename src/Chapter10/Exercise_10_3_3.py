# Exercise 10.3-3 — CLRS
# EN: Demonstrate that ALLOCATE-OBJECT and FREE-OBJECT do not need to initialize or update prev.
# PL: Udowodnij, że ALLOCATE-OBJECT i FREE-OBJECT nie muszą inicjować ani aktualizować prev.

class MemoryManager:
    def __init__(self, size):
        self.key = [None] * size
        self.next = [None] * size
        self.prev = [None] * size  # prev nieużywane w zarządzaniu pamięcią
        self.free = 0
        for i in range(size - 1):
            self.next[i] = i + 1
        self.next[size - 1] = None

    def allocate_object(self, key_value):
        if self.free is None:
            raise MemoryError("Brak pamięci")
        x = self.free
        self.free = self.next[x]
        self.key[x] = key_value
        # prev[x] nie jest ustawiane — dowód, że nie jest potrzebne
        return x

    def free_object(self, x):
        self.next[x] = self.free
        self.key[x] = None
        self.free = x
        # prev[x] nie jest modyfikowane — nie wpływa na poprawność

    def debug_state(self):
        return {
            "key": self.key,
            "next": self.next,
            "prev": self.prev,
            "free": self.free
        }

if __name__ == "__main__":
    mm = MemoryManager(4)
    print("Stan początkowy:", mm.debug_state())

    i1 = mm.allocate_object("A")
    i2 = mm.allocate_object("B")
    print("Po alokacji A i B:", mm.debug_state())

    mm.free_object(i1)
    print("Po zwolnieniu A:", mm.debug_state())

    i3 = mm.allocate_object("C")
    print("Po alokacji C (na miejscu A):", mm.debug_state())

    print("Wartość prev:", mm.prev)  # prev nigdy nie było używane
