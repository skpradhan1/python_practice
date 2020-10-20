from tree.BinarySearchTree import BinarySearchTree
from tree.bst_display import display
from tree.Node import Node


def find_min(root:Node):
    if root is None:
        return -1
    elif root.leftChild is None:
        return root.val
    else:
        return find_min(root.leftChild)


bst = BinarySearchTree(50)

bst.insert_rec(31)
bst.insert(9)
bst.insert(32)
bst.insert(5)
bst.insert(23)
bst.insert(54)
bst.insert(62)
bst.insert(57)
bst.insert(78)
bst.insert(63)
bst.insert(75)

print(find_min(bst.root))