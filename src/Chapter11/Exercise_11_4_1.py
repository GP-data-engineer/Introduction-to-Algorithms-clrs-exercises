# Exercise 11.4-1 — CLRS
# EN: Insert keys into a hash table of size m=11 using open addressing:
#     linear probing, quadratic probing, and double hashing.
# PL: Wstaw klucze do tablicy haszującej m=11 używając adresowania otwartego:
#     adresowania liniowego, kwadratowego i podwójnego haszowania.

class OpenAddressingHash:
    def __init__(self, m):
        self.m = m
        self.T = [None] * m

    def h_linear(self, k, i):
        return (k + i) % self.m

    def h_quadratic(self, k, i, c1=1, c2=3):
        return (k + c1 * i + c2 * i * i) % self.m

    def h_double(self, k, i):
        h1 = k % self.m
        h2 = 1 + (k % (self.m - 1))
        return (h1 + i * h2) % self.m

    def insert(self, k, method="linear"):
        for i in range(self.m):
            if method == "linear":
                pos = self.h_linear(k, i)
            elif method == "quadratic":
                pos = self.h_quadratic(k, i)
            elif method == "double":
                pos = self.h_double(k, i)
            else:
                raise ValueError("Unknown method")

            if self.T[pos] is None:
                self.T[pos] = k
                return pos
        raise OverflowError("Hash table overflow")

if __name__ == "__main__":
    keys = [10, 22, 31, 4, 15, 28, 17, 88, 59]

    print("=== Linear Probing ===")
    h1 = OpenAddressingHash(11)
    for k in keys:
        h1.insert(k, "linear")
    print(h1.T)

    print("\n=== Quadratic Probing ===")
    h2 = OpenAddressingHash(11)
    for k in keys:
        h2.insert(k, "quadratic")
    print(h2.T)

    print("\n=== Double Hashing ===")
    h3 = OpenAddressingHash(11)
    for k in keys:
        h3.insert(k, "double")
    print(h3.T)
