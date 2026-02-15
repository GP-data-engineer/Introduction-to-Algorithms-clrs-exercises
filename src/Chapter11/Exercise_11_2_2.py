# Exercise 11.2-2 (CLRS)
# PL:
# Zilustruj wstawianie elementów do tablicy z haszowaniem (metoda łańcuchowa).
#
# EN:
# Illustrate insertion into a hash table with chaining.

class HashTableChaining:

    def __init__(self, m):
        self.m = m
        self.table = [[] for _ in range(m)]

    def h(self, k):
        return k % self.m

    def insert(self, key):
        index = self.h(key)
        self.table[index].append(key)

    def get_table(self):
        return self.table


if __name__ == "__main__":
    keys = [5, 28, 19, 15, 20, 33, 12, 17, 10]
    ht = HashTableChaining(9)
    for k in keys:
        ht.insert(k)
    print("Hash table:", ht.get_table())
