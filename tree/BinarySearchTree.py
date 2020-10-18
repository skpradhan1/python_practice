from tree.Node import Node


class BinarySearchTree:
    def __init__(self, val):
        self.root = Node(val)

    def insert(self, val):
        if self.root:
            self.root.insert(val)
        else:
            self.root = Node(val)

    def insert_rec(self, val):
        if self.root:
            self.root.insert_rec(val)
        else:
            self.root = Node(val)

    def search(self,val):
        if self.root:
            return self.root.search(val)
        else:
            return False