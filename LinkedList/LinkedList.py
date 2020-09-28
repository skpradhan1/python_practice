from Node import Node


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

    def insert_at_tail(self, data):
        head = self.get_head()
        prev = None
        if head is None:
            self.head_node = Node(data)
        else:
            while head is not None:
                prev = head
                head = head.next_element
            temp = Node(data)
            prev.next_element = temp

    def search(self, value):
        temp = self.get_head()
        while temp:
            if temp.data == value:
                return True
            temp = temp.next_element
        return False

    def delete_at_head(self):
        head = self.get_head()
        if head is None:
            return False
        self.head_node = head.next_element
        return

    def delete(self, val):
        temp = self.get_head()
        prev = None

        if temp.data is val:
            self.delete_at_head()
            return True
        else:
            while temp is not None:
                if temp.data is val:
                    prev.next_element = temp.next_element
                    temp.next_element = None
                    return True
                else:
                    prev = temp
                    temp = temp.next_element
            return False

    def length(self):
        curr = self.get_head()
        length = 0
        while curr:
            length += 1
            curr = curr.next_element
        return length

    def print_list(self):
        if self.is_empty():
            print('List is empty')
            return False
        else:
            tmp = self.head_node
            while tmp.next_element is not None:
                print(tmp.data, end=" -> ")
                tmp = tmp.next_element
            print(tmp.data, end=" -> None")
            print('')
            return True
