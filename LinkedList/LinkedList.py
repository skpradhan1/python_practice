from LinkedList.Node import Node


class LinkedList:

    def __init__(self):
        self.head_node = None

    def get_head(self):
        return self.head_node

    def is_empty(self):
        if self.head_node is None:
            return True
        else:
            return False

    def insert_at_head(self, data):
        node = Node(data)
        node.next_element = self.head_node
        self.head_node = node
        return self.head_node

    def print_list(self):
        if self.is_empty():
            print('List is empty')
            return False
        else:
            tmp = self.head_node
            while tmp.next_element is not None:
                print(tmp.data, end= " -> ")
                tmp = tmp.next_element
            print(tmp.data, end=" -> None")
            return True


