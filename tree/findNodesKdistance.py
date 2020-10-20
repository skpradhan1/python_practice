from tree.BinarySearchTree import BinarySearchTree
from tree.bst_display import display
from tree.Node import Node


def traverse(root: Node, k, n, lst):
    if root is None:
        return None

    if k == n:
        lst.append(root.val)

    if root is not None:
        k = k + 1
        traverse(root.leftChild, k, n, lst)
        traverse(root.rightChild, k, n, lst)

    return lst


def findKNodes(root, n):
    k = 0
    lst = []
    lst = traverse(root, k, n, lst)
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

print(findKNodes(bst.root,2))