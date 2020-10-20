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

    def delete(self,val):
        if val < self.val:
            if self.leftChild:
                self.leftChild = self.leftChild.delete(val)
            else:
                print(str(val) + " not found in the tree")
                return None
        elif val > self.val:
            if self.rightChild:
                self.rightChild = self.rightChild.delete(val)
            else:
                print(str(val) + " not found in the tree")
                return None
        else:
            if self.leftChild is None and self.rightChild is None:
                self = None
                return None
            elif self.leftChild is None:
                tmp = self.rightChild
                self = None
                return tmp
            elif self.rightChild is None:
                tmp = self.leftChild
                self = None
                return tmp
            else:
                current = self.rightChild
                while current.leftChild is not None:
                    current = current.leftChild

                self.val = current.val
                self.rightChild = self.rightChild.delete(current.val)

        return self

