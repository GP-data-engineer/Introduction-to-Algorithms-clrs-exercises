# Exercise 10.4-6 — CLRS_
# EN: Use two pointers and one boolean per node to access parent and all children in a rooted tree.
# PL: Użyj dwóch wskaźników i jednej zmiennej boolowskiej w węźle, aby wyznaczać ojca i wszystkich synów.

class CompactNode:
    def __init__(self, key):
        self.key = key
        self.parent = None      # Wskaźnik na ojca
        self.link = None        # Węzeł: dla ojca — pierwszy syn, dla syna — następny brat w liście cyklicznej
        self.is_parent = False  # True, jeśli węzeł jest ojcem (ma listę dzieci)

def add_children(parent, children):
    # Tworzymy cykliczną listę dzieci
    if not children:
        return
    parent.is_parent = True
    parent.link = children[0]
    n = len(children)
    for i, child in enumerate(children):
        child.parent = parent
        child.is_parent = False
        child.link = children[(i + 1) % n]  # Cykliczna lista rodzeństwa

def get_parent(node):
    # Zwraca ojca w czasie O(1)
    return node.parent

def get_children(parent):
    # Zwraca listę dzieci w czasie proporcjonalnym do ich liczby
    if not parent.is_parent or parent.link is None:
        return []
    result = []
    start = parent.link
    current = start
    while True:
        result.append(current)
        current = current.link
        if current is start:
            break
    return result

if __name__ == "__main__":
    root = CompactNode(1)
    c1 = CompactNode(2)
    c2 = CompactNode(3)
    c3 = CompactNode(4)
    add_children(root, [c1, c2, c3])
    print("Ojciec 2:", get_parent(c1).key)
    print("Dzieci korzenia:", [c.key for c in get_children(root)])
