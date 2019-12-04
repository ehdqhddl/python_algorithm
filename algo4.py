# Algo 4
# Linked List 실습 및 구현


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class NodeManagement:
    def __init__(self, data):
        self.head = Node(data)

    def add_node(self, data):
        if self is None:
            self.head = Node(data)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(data)

    def show_node(self):
        if self.head is None:
            print("Nothing here.")
        else:
            node = self.head
            while node:
                print(node.data)
                node = node.next

    def del_node(self, data):
        if self.head is None:
            print("Nothing here.")
        else:
            node = self.head
            prev_node = None

            while node:
                if node.data == data:
                    if prev_node is not None:
                        prev_node.next = node.next
                        node = None
                    else:
                        self.head = node.next
                        node = None
                else:
                    prev_node = node
                    node = node.next


linkedList = NodeManagement(0)
linkedList.show_node()
print("--------------------")
for index in range(1, 10):
    linkedList.add_node(index)
linkedList.show_node()
print("--------------------")
for index in range(0, 10):
    linkedList.del_node(index)
linkedList.show_node()
print("--------------------")
