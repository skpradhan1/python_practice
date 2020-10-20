from tree.BinarySearchTree import BinarySearchTree
from tree.bst_display import display

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

display(bst.root)
bst.delete(9)
display(bst.root)

bst.delete(62)
display(bst.root)