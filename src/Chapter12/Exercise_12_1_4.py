# Exercise 12.1-4 — CLRS
# EN: Recursive preorder and postorder traversals.
# PL: Rekurencyjne przejścia preorder i postorder.

class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

def preorder(root):
    if root is None:
        return []
    return [root.key] + preorder(root.left) + preorder(root.right)

def postorder(root):
    if root is None:
        return []
    return postorder(root.left) + postorder(root.right) + [root.key]

if __name__ == "__main__":
    root = Node(10, Node(5), Node(15))
    print("Preorder:", preorder(root))
    print("Postorder:", postorder(root))
