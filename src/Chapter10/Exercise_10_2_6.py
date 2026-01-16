# Exercise 10.2-6 — CLRS
# EN: Design a list-based UNION operation for disjoint sets in O(1) time.
# PL: Zaprojektuj operację UNION dla rozłącznych zbiorów w czasie O(1).

class Node:
    def __init__(self, key):
        self.key = key
        self.next = None

class SetList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, key):
        new_node = Node(key)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def union(self, other):
        # Łączymy listy w czasie O(1)
        if not self.head:
            self.head = other.head
            self.tail = other.tail
        elif other.head:
            self.tail.next = other.head
            self.tail = other.tail
        other.head = other.tail = None

    def to_list(self):
        result = []
        x = self.head
        while x:
            result.append(x.key)
            x = x.next
        return result

if __name__ == "__main__":
    s1 = SetList()
    s2 = SetList()
    for x in [1, 2, 3]:
        s1.insert(x)
    for y in [4, 5]:
        s2.insert(y)
    s1.union(s2)
    print("UNION:", s1.to_list())
