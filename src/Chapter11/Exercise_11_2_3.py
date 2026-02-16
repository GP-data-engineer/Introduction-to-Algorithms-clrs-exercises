# Exercise 11.2-3 (CLRS)
# PL:
# Wpływ sortowania list łańcuchowych na czas operacji.
#
# EN:
# Effect of keeping chains sorted on operation complexity.

class SortedChainHashTable:

    def __init__(self, m):
        self.m = m
        self.table = [[] for _ in range(m)]

    def h(self, k):
        return k % self.m

    def insert(self, key):
        index = self.h(key)
        chain = self.table[index]
        chain.append(key)
        chain.sort()  # maintain sorted order

    def search(self, key):
        index = self.h(key)
        return key in self.table[index]

    def delete(self, key):
        index = self.h(key)
        if key in self.table[index]:
            self.table[index].remove(key)
            return True
        return False


if __name__ == "__main__":
    ht = SortedChainHashTable(5)
    ht.insert(10)
    ht.insert(5)
    print("Search 10:", ht.search(10))
