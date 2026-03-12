# Exercise 12.2-2 — CLRS
# EN: Recursive TREE-MINIMUM and TREE-MAXIMUM procedures.
# PL: Rekurencyjne procedury TREE-MINIMUM i TREE-MAXIMUM.

class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

def tree_minimum(node):
    if node.left is None:
        return node
    return tree_minimum(node.left)

def tree_maximum(node):
    if node.right is None:
        return node
    return tree_maximum(node.right)

if __name__ == "__main__":
    root = Node(10, Node(5), Node(15))
    print("Minimum:", tree_minimum(root).key)
    print("Maximum:", tree_maximum(root).key)
