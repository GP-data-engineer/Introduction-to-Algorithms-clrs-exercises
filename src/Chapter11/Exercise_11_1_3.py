# Exercise 11.1-3 — CLRS
# EN: Direct-address table where keys need not be distinct and each element has extra data.
#     INSERT, DELETE (by pointer), and SEARCH must run in O(1).
# PL: Tablica z adresowaniem bezpośrednim z powtarzającymi się kluczami i dodatkowymi danymi.
#     INSERT, DELETE (po wskaźniku) i SEARCH mają działać w czasie O(1).

class Node:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.next = None   # następny w kubełku
        self.prev = None   # poprzedni w kubełku

class DirectAddressMulti:
    def __init__(self, m):
        # Tablica kubełków — każdy indeks to lista elementów o danym kluczu
        self.m = m
        self.T = [None] * m

    def insert(self, key, data):
        # Wstawiamy nowy element na początek listy kubełka
        if not (0 <= key < self.m):
            raise ValueError("Klucz poza zakresem")
        node = Node(key, data)
        head = self.T[key]
        node.next = head
        if head is not None:
            head.prev = node
        self.T[key] = node
        return node  # zwracamy wskaźnik do obiektu

    def search(self, key):
        # Zwracamy pierwszy element o danym kluczu (lub None)
        if not (0 <= key < self.m):
            return None
        return self.T[key]

    def delete(self, node):
        # Usuwamy element na podstawie wskaźnika do niego
        key = node.key
        if node.prev is not None:
            node.prev.next = node.next
        else:
            # node był głową listy kubełka
            self.T[key] = node.next
        if node.next is not None:
            node.next.prev = node.prev

if __name__ == "__main__":
    d = DirectAddressMulti(10)
    n1 = d.insert(3, "a")
    n2 = d.insert(3, "b")
    print("Pierwszy element o kluczu 3:", d.search(3).data)
    d.delete(n2)
    print("Po usunięciu n2, pierwszy o kluczu 3:", d.search(3).data)
