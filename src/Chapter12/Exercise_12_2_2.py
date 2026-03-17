# PL: Rekurencyjne TREE-MINIMUM i TREE-MAXIMUM
# EN: Recursive tree minimum and maximum

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def tree_minimum(x):
    if x.left is None:
        return x
    return tree_minimum(x.left)


def tree_maximum(x):
    if x.right is None:
        return x
    return tree_maximum(x.right)


if __name__ == "__main__":
    root = Node(10)
    root.left = Node(5)
    root.right = Node(20)
    print(tree_minimum(root).key)