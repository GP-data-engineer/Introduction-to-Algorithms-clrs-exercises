# Exercise 11.1-1 — CLRS
# EN: Direct-addressed set S in table T[0..m-1]; find the largest element of S.
# PL: Zbiór dynamiczny S w tablicy T[0..m-1] z adresowaniem bezpośrednim; znajdź największy element S.

class DirectAddressSet:
    def __init__(self, m):
        # Tablica T przechowuje True/False — czy element o danym kluczu należy do S
        self.m = m
        self.T = [False] * m

    def insert(self, k):
        # Wstawiamy klucz k do zbioru
        if 0 <= k < self.m:
            self.T[k] = True

    def delete(self, k):
        # Usuwamy klucz k ze zbioru
        if 0 <= k < self.m:
            self.T[k] = False

    def search(self, k):
        # Sprawdzamy, czy k należy do zbioru
        return 0 <= k < self.m and self.T[k]

    def max_element(self):
        # Szukamy największego k, dla którego T[k] == True
        for k in range(self.m - 1, -1, -1):
            if self.T[k]:
                return k
        return None  # zbiór pusty

if __name__ == "__main__":
    s = DirectAddressSet(10)
    s.insert(3)
    s.insert(7)
    s.insert(5)
    print("Największy element zbioru S:", s.max_element())
