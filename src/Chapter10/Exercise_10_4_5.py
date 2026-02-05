# Exercise 10.4-5 — CLRS
# EN: Non-recursive O(n) procedure with O(1) extra space printing all keys of a binary tree (Morris traversal).
# PL: Nierekurencyjna procedura O(n) ze stałą pamięcią wypisująca wszystkie klucze drzewa binarnego (przejście Morrisa).

class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

def morris_inorder_keys(root):
    # Przejście Morrisa: inorder bez stosu i bez rekurencji
    result = []
    current = root
    while current:
        if current.left is None:
            result.append(current.key)
            current = current.right
        else:
            # Szukamy poprzednika w inorder
            pre = current.left
            while pre.right and pre.right is not current:
                pre = pre.right
            if pre.right is None:
                pre.right = current  # Tworzymy tymczasowe łącze
                current = current.left
            else:
                pre.right = None     # Usuwamy tymczasowe łącze
                result.append(current.key)
                current = current.right
    return result

if __name__ == "__main__":
    root = Node(2, Node(1), Node(3))
    print("Klucze (Morris inorder):", morris_inorder_keys(root))
