# Exercise 10.2-2 — CLRS
# EN: Implement a stack using a singly linked list. PUSH and POP should run in O(1) time.
# PL: Zaimplementuj stos za pomocą listy jednokierunkowej. Operacje PUSH i POP powinny działać w czasie O(1).

class Node:
    def __init__(self, key):
        self.key = key
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, key):
        # Dodajemy element na początek listy
        new_node = Node(key)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        # Usuwamy element z początku listy
        if self.top is None:
            raise IndexError("pop from empty stack")
        key = self.top.key
        self.top = self.top.next
        return key

    def is_empty(self):
        return self.top is None

if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    print("POP:", s.pop())  # powinno wypisać 3
