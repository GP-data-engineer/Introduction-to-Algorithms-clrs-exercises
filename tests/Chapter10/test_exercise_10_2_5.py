# Exercise 10.2-5 — CLRS
# EN: Implement dictionary operations using a cyclic singly linked list.
# PL: Zaimplementuj operacje słownikowe INSERT, DELETE, SEARCH na cyklicznej liście jednokierunkowej.

class Node:
    def __init__(self, key):
        self.key = key
        self.next = None

class CyclicListDict:
    def __init__(self):
        self.nil = Node(None)
        self.nil.next = self.nil

    def insert(self, key):
        new_node = Node(key)
        new_node.next = self.nil.next
        self.nil.next = new_node

    def search(self, key):
        self.nil.key = key
        x = self.nil.next
        while x.key != key:
            x = x.next
        return x if x != self.nil else None

    def delete(self, key):
        prev = self.nil
        curr = self.nil.next
        while curr != self.nil and curr.key != key:
            prev = curr
            curr = curr.next
        if curr != self.nil:
            prev.next = curr.next

if __name__ == "__main__":
    d = CyclicListDict()
    d.insert(10)
    d.insert(20)
    d.insert(30)
    d.delete(20)
    print("Szukam 20:", "Znaleziono" if d.search(20) else "Nie znaleziono")
