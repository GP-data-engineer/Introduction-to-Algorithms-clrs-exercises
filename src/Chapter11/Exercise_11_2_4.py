# Exercise 11.2-4 (CLRS)
# PL:
# Przydzielanie i zwalnianie pamięci w obrębie tej samej tablicy.
#
# EN:
# Memory allocation and deallocation inside the same hash table.

class FreeListHashTable:

    def __init__(self, m):
        self.m = m
        self.table = [None] * m
        self.free_list = list(range(m))

    def allocate(self, key):
        if not self.free_list:
            raise Exception("No free space")
        index = self.free_list.pop()
        self.table[index] = key
        return index

    def free(self, index):
        self.table[index] = None
        self.free_list.append(index)


if __name__ == "__main__":
    ht = FreeListHashTable(5)
    idx = ht.allocate(10)
    print("Allocated at:", idx)
    ht.free(idx)
    print("Freed.")
