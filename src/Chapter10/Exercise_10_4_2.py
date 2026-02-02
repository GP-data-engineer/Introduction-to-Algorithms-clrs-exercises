# Exercise 10.4-2 — CLRS
# EN: Recursive O(n) procedure printing all keys of a binary tree.
# PL: Rekurencyjna procedura O(n) wypisująca wszystkie klucze drzewa binarnego.

class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

def recursive_print_keys(root):
    # Preorder: korzeń, lewo, prawo
    result = []
    def dfs(node):
        if node is None:
            return
        result.append(node.key)
        dfs(node.left)
        dfs(node.right)
    dfs(root)
    return result

if __name__ == "__main__":
    root = Node(8, Node(3), Node(10))
    print("Klucze (rekurencyjnie):", recursive_print_keys(root))
