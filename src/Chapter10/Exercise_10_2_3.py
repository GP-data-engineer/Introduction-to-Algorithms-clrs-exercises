# Exercise 10.2-3 — CLRS
# EN: Implement a queue using a singly linked list. ENQUEUE and DEQUEUE should run in O(1) time.
# PL: Zaimplementuj kolejkę za pomocą listy jednokierunkowej. Operacje ENQUEUE i DEQUEUE powinny działać w czasie O(1).

class Node:
    def __init__(self, key):
        self.key = key
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, key):
        # Dodajemy na koniec listy
        new_node = Node(key)
        if self.tail:
            self.tail.next = new_node
        else:
            self.head = new_node
        self.tail = new_node

    def dequeue(self):
        # Usuwamy z początku listy
        if self.head is None:
            raise IndexError("dequeue from empty queue")
        key = self.head.key
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return key

    def is_empty(self):
        return self.head is None

if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    print("DEQUEUE:", q.dequeue())  # powinno wypisać 1
