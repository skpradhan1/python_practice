from tree.BinarySearchTree import BinarySearchTree
import random
from tree.bst_display import display

BST = BinarySearchTree(50)
for _ in range(15):
    ele = random.randint(0, 100)
    BST.insert(ele)

# We have hidden the code for this function but it is available for use!
display(BST.root)
print('\n')

print(BST.search(15))
print(BST.search(50))