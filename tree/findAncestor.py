from tree.BinarySearchTree import BinarySearchTree
from tree.bst_display import display
from tree.Node import Node


def find_ancestor_helper(root:Node, k, lst):
    if root is not None:
        if k > root.val:
            if find_ancestor_helper(root.rightChild, k, lst):
                lst.append(root.val)
                return True
        elif k < root.val:
            if find_ancestor_helper(root.leftChild, k, lst):
                lst.append(root.val)
                return True
        elif root.val is k:
            return True
        else:
            return False
        return lst
    else:
        return False

def findAncestor(root:Node,k):
    lst=[]
    if root is not None:
        find_ancestor_helper(root,k,lst)
    return lst

bst = BinarySearchTree(6)
bst.insert(4)
bst.insert(2)
bst.insert(5)
bst.insert(9)
bst.insert(8)
bst.insert(12)
bst.insert(10)
bst.insert(14)

print(findAncestor(bst.root,10))
