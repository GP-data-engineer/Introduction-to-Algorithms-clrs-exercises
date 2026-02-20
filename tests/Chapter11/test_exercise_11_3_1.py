# Exercise 11.3-1 (CLRS)
# PL:
# Mamy listę długości n, gdzie każdy element przechowuje klucz k
# oraz wartość funkcji haszującej h(k).
# Jak wykorzystać h(k) do przyspieszenia wyszukiwania?
#
# EN:
# Given a list of length n where each element stores key k and its hash value h(k).
# How can we use stored hash values to speed up search?

class HashedList:

    def __init__(self):
        self.data = []

    def insert(self, key, hash_value):
        self.data.append((key, hash_value))

    def search(self, key, hash_value):
        # first compare hash values, then actual keys
        for k, h in self.data:
            if h == hash_value:  # quick rejection if hashes differ
                if k == key:
                    return True
        return False


if __name__ == "__main__":
    hl = HashedList()
    hl.insert("abc", hash("abc"))
    print("Found:", hl.search("abc", hash("abc")))
