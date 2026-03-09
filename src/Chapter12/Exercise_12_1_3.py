# Exercise 12.1-3 — CLRS
# EN: Non-recursive inorder traversal using a stack.
# PL: Nierekurencyjne przejście inorder z użyciem stosu.

class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

def inorder_nonrecursive(root):
    result = []
    stack = []
    current = root

    while current or stack:
        while current:
            stack.append(current)
            current = current.left

        current = stack.pop()
        result.append(current.key)
        current = current.right

    return result

if __name__ == "__main__":
    root = Node(10, Node(5), Node(15))
    print("Inorder:", inorder_nonrecursive(root))
