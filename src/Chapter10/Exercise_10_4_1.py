# Exercise 10.4-1 — CLRS
# EN: Build the binary tree from the given table and provide a traversal.
# PL: Zbuduj drzewo binarne z podanej tabeli i wypisz jego klucze.

from dataclasses import dataclass
from typing import Optional, List, Dict

@dataclass
class Node:
    key: int
    left: Optional["Node"] = None
    right: Optional["Node"] = None

def build_tree_from_table() -> Node:
    # Tworzymy węzły według indeksów
    table = {
        1: (12, 7, 3),
        2: (15, 4, None),
        3: (4, 10, None),
        4: (10, 5, 9),
        5: (6, None, None),
        6: (8, 1, 2),
        7: (7, None, None),
        8: (14, 6, 2),
        9: (21, None, None),
        10: (5, None, None),
    }
    nodes: Dict[int, Node] = {i: Node(key=v[0]) for i, v in table.items()}
    for i, (key, l, r) in table.items():
        if l is not None:
            nodes[i].left = nodes[l]
        if r is not None:
            nodes[i].right = nodes[r]
    # Korzeń ma indeks 6
    return nodes[6]

def preorder(root: Optional[Node]) -> List[int]:
    # Proste przejście preorder
    if root is None:
        return []
    return [root.key] + preorder(root.left) + preorder(root.right)

if __name__ == "__main__":
    root = build_tree_from_table()
    print("Preorder drzewa (korzeń indeks 6):", preorder(root))
