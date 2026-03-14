# Exercise 12.2-3 — CLRS
# EN: Implement TREE-PREDECESSOR procedure.
# PL: Zaimplementuj procedurę TREE-PREDECESSOR.

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None

def tree_predecessor(x):
    if x.left:
        return tree_maximum(x.left)
    y = x.parent
    while y and x == y.left:
        x = y
        y = y.parent
    return y

def tree_maximum(node):
    while node.right:
        node = node.right
    return node

if __name__ == "__main__":
    a = Node(10)
    b = Node(5)
    c = Node(15)
    a.left = b
    a.right = c
    b.parent = a
    c.parent = a
    print("Poprzednik 15:", tree_predecessor(c).key)
