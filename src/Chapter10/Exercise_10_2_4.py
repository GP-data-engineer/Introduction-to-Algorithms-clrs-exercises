# Exercise 10.2-4 — CLRS
# EN: Eliminate the check x ≠ L.nil in LIST-SEARCH loop.
# PL: Wyeliminuj sprawdzanie warunku x ≠ L.nil w pętli LIST-SEARCH.

class Node:
    def __init__(self, key):
        self.key = key
        self.next = None

class LinkedList:
    def __init__(self):
        self.nil = Node(None)  # Strażnik
        self.nil.next = self.nil

    def insert(self, key):
        new_node = Node(key)
        new_node.next = self.nil.next
        self.nil.next = new_node

    def search(self, k):
        # Dodajemy strażnika z kluczem k
        self.nil.key = k
        x = self.nil.next
        while x.key != k:
            x = x.next
        return x if x != self.nil else None

if __name__ == "__main__":
    lista = LinkedList()
    lista.insert(10)
    lista.insert(20)
    lista.insert(30)
    wynik = lista.search(20)
    print("Znaleziono:", wynik.key if wynik else "Brak")
