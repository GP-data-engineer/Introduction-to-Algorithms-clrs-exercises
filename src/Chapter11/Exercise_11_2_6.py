# Exercise 11.2-6 (CLRS)
# PL:
# Procedura losowego wyboru klucza z tablicy z haszowaniem.
#
# EN:
# Procedure returning random key in expected O(L(1+1/alpha)) time.

import random


class RandomHashTable:

    def __init__(self, table):
        self.table = table
        self.m = len(table)

    def random_key(self):
        non_empty = [chain for chain in self.table if chain]
        if not non_empty:
            return None
        chain = random.choice(non_empty)
        return random.choice(chain)


if __name__ == "__main__":
    table = [[1, 2], [], [3], [], [4, 5]]
    ht = RandomHashTable(table)
    print("Random key:", ht.random_key())
