# Exercise 10.2-7 — CLRS
# EN: Write a non-recursive procedure to reverse a singly linked list in Θ(n) time using constant space.
# PL: Napisz nierekurencyjną procedurę odwracającą listę jednokierunkową w czasie Θ(n) przy stałej pamięci.

class Node:
    def __init__(self, key):
        self.key = key
        self.next = None

class SinglyList:
    def __init__(self):
        self.head = None

    def insert(self, key):
        new_node = Node(key)
        new_node.next = self.head
        self.head = new_node

    def reverse(self):
        prev = None
        curr = self.head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        self.head = prev

    def to_list(self):
        result = []
        x = self.head
        while x:
            result.append(x.key)
            x = x.next
        return result

if __name__ == "__main__":
    l = SinglyList()
    for i in range(1, 6):
        l.insert(i)
    print("Przed odwróceniem:", l.to_list())
    l.reverse()
    print("Po odwróceniu:", l.to_list())