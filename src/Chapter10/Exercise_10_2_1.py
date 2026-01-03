# Exercise 10.2-1 (EN): Show how INSERT on a singly linked list can work in O(1),
# and discuss DELETE. INSERT is O(1) if we insert after a given node; DELETE is
# O(1) only if we know the previous node.
# Exercise 10.2-1 (PL): Pokaż, kiedy INSERT na liście jednokierunkowej działa w O(1)
# i omów DELETE. INSERT jest O(1), jeśli wstawiamy po danym węźle; DELETE jest
# O(1) tylko gdy znamy poprzednik usuwanego węzła .

class Node:
    # Węzeł listy jednokierunkowej / Singly linked list node
    def __init__(self, key):
        self.key = key
        self.next = None


class SinglyLinkedList:
    # Prosta lista jednokierunkowa z dostępem do głowy / Simple singly linked list with head
    def __init__(self):
        self.head = None

    def insert_after(self, node, new_node):
        # Wstawia new_node po node w czasie O(1), zakładając znany węzeł / O(1) insert after given node
        new_node.next = node.next
        node.next = new_node

    def insert_head(self, new_node):
        # Wstawia new_node na początek listy w czasie O(1) / O(1) insert at head
        new_node.next = self.head
        self.head = new_node

    def delete_after(self, node):
        # Usuwa węzeł po node w czasie O(1), jeśli istnieje / O(1) delete after given node
        if node is None or node.next is None:
            return None
        to_delete = node.next
        node.next = to_delete.next
        to_delete.next = None
        return to_delete

    def to_list(self):
        # Konwersja listy jednokierunkowej do listy Pythona / Convert linked list to Python list
        result = []
        curr = self.head
        while curr:
            result.append(curr.key)
            curr = curr.next
        return result


if __name__ == "__main__":
    # Demonstracja INSERT i DELETE na liście jednokierunkowej / Demo of INSERT and DELETE
    lst = SinglyLinkedList()
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    lst.insert_head(n3)
    lst.insert_head(n2)
    lst.insert_head(n1)
    print("Lista po wstawieniach na głowę:", lst.to_list())
    lst.insert_after(n2, Node(5))
    print("Lista po INSERT_AFTER(2, 5):", lst.to_list())
    lst.delete_after(n2)
    print("Lista po DELETE_AFTER(2):", lst.to_list())
