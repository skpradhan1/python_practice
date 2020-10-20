from tree.BinarySearchTree import BinarySearchTree
from tree.bst_display import display
from tree.Node import Node


def find_helper(root:Node,lst):
    if root is not None:
        find_helper(root.leftChild,lst)
        lst.append(root.val)
        find_helper(root.rightChild,lst)
    return lst


def findKthMax(root:Node, k):
    if root is not None:
        lst = []
        lst = find_helper(root,lst)

    return lst[-k]

bst = BinarySearchTree(6)
bst.insert(4)
bst.insert(2)
bst.insert(5)
bst.insert(9)
bst.insert(8)
bst.insert(12)
bst.insert(10)
bst.insert(14)

print(findKthMax(bst.root,3))