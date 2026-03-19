# PL: TREE-PREDECESSOR
# EN: Find predecessor in BST

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None


def tree_maximum(x):
    while x.right:
        x = x.right
    return x


def tree_predecessor(x):
    if x.left:
        return tree_maximum(x.left)

    y = x.parent
    while y and x == y.left:
        x = y
        y = y.parent
    return y


if __name__ == "__main__":
    root = Node(10)
    root.left = Node(5)
    root.left.parent = root
    print(tree_predecessor(root).key if tree_predecessor(root) else None)
