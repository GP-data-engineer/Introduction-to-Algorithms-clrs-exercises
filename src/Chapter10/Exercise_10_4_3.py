# Exercise 10.4-3 — CLRS
# EN: Non-recursive O(n) procedure using a stack to print all keys of a binary tree.
# PL: Nierekurencyjna procedura O(n) używająca stosu do wypisania wszystkich kluczy drzewa binarnego.

class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

def iterative_print_keys(root):
    # Preorder z użyciem stosu
    if root is None:
        return []
    stack = [root]
    result = []
    while stack:
        node = stack.pop()
        result.append(node.key)
        # Najpierw prawe, potem lewe, aby lewe było przetwarzane pierwsze
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return result

if __name__ == "__main__":
    root = Node(1, Node(2), Node(3))
    print("Klucze (nierekurencyjnie, stos):", iterative_print_keys(root))
