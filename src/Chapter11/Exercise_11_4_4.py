# Exercise 10.4-4 — CLRS
# EN: O(n) procedure printing all keys of a rooted tree in left-child/right-sibling representation.
# PL: Procedura O(n) wypisująca wszystkie klucze drzewa ukorzenionego w reprezentacji „na lewo syn, na prawo brat”.

class LCNode:
    def __init__(self, key, left_child=None, right_sibling=None):
        self.key = key
        self.left_child = left_child
        self.right_sibling = right_sibling

def print_lcrs_keys(root):
    # Preorder: węzeł, jego dzieci (rekurencyjnie), potem rodzeństwo
    result = []
    def visit(node):
        if node is None:
            return
        result.append(node.key)
        visit(node.left_child)
        visit(node.right_sibling)
    visit(root)
    return result

if __name__ == "__main__":
    # Przykład: korzeń z dwoma synami
    child2 = LCNode(3)
    child1 = LCNode(2, right_sibling=child2)
    root = LCNode(1, left_child=child1)
    print("Klucze (LCRS):", print_lcrs_keys(root))
