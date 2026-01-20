# Exercise 10.2-8 — CLRS
# EN: Implement a doubly linked list using one pointer per node: x.np = x.next XOR x.prev.
# PL: Zaimplementuj listę dwukierunkową z jednym wskaźnikiem x.np = x.next XOR x.prev.

class XORNode:
    def __init__(self, key):
        self.key = key
        self.np = 0  # XOR of prev and next

class XORLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.__nodes = {}  # id → node

    def _xor(self, a, b):
        return a ^ b

    def insert(self, key):
        new_node = XORNode(key)
        new_id = id(new_node)
        self.__nodes[new_id] = new_node

        if self.head is None:
            self.head = self.tail = new_node
        else:
            tail_id = id(self.tail)
            new_node.np = tail_id
            self.tail.np ^= new_id
            self.tail = new_node

    def traverse(self):
        result = []
        prev_id = 0
        node = self.head
        while node:
            result.append(node.key)
            next_id = self._xor(prev_id, node.np)
            prev_id = id(node)
            node = self.__nodes.get(next_id, None)
        return result

    def search(self, key):
        prev_id = 0
        node = self.head
        while node:
            if node.key == key:
                return node
            next_id = self._xor(prev_id, node.np)
            prev_id = id(node)
            node = self.__nodes.get(next_id, None)
        return None

    def delete(self, key):
        prev_id = 0
        node = self.head
        while node:
            if node.key == key:
                next_id = self._xor(prev_id, node.np)
                prev_node = self.__nodes.get(prev_id, None)
                next_node = self.__nodes.get(next_id, None)

                if prev_node:
                    prev_node.np ^= id(node) ^ next_id
                else:
                    self.head = next_node

                if next_node:
                    next_node.np ^= id(node) ^ prev_id
                else:
                    self.tail = prev_node

                del self.__nodes[id(node)]
                return True
            next_id = self._xor(prev_id, node.np)
            prev_id = id(node)
            node = self.__nodes.get(next_id, None)
        return False

    def reverse(self):
        # O(1) — zamiana head i tail
        self.head, self.tail = self.tail, self.head

if __name__ == "__main__":
    lista = XORLinkedList()
    for x in [10, 20, 30, 40]:
        lista.insert(x)
    print("Przed odwróceniem:", lista.traverse())
    lista.reverse()
    print("Po odwróceniu:", lista.traverse())
