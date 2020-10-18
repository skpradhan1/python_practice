class Node:
    def __init__(self,val):
        self.val = val
        self.leftChild = None
        self.rightChild = None
        self.parent = None

    def insert(self, val):
        current = self
        parent = None
        while current:
            if val < current.val:
                parent = current
                current = current.leftChild
            else:
                parent = current
                current = current.rightChild

        if val < parent.val:
            parent.leftChild = Node(val)
        else:
            parent.rightChild = Node(val)

    def insert_rec(self, val):
        if val < self.val:
            if self.leftChild:
                self.leftChild.insert_rec(val)
            else:
                self.leftChild = Node(val)

        else:
            if self.rightChild:
                self.rightChild.insert_rec(val)
            else:
                self.rightChild = Node(val)

    def search(self, val):
        if val < self.val:
            if self.leftChild:
                self.leftChild.search(val)
            else:
                return False
        elif val > self.val:
            if self.rightChild:
                self.rightChild.search(val)
            else:
                return False
        else:
            return True
