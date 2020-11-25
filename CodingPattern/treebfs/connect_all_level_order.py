from __future__ import print_function
from collections import deque


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right, self.next = None, None, None

  # tree traversal using 'next' pointer
  def print_tree(self):
    print("Traversal using 'next' pointer: ", end='')
    current = self
    while current:
      print(str(current.val) + " ", end='')
      current = current.next


def connect_all_siblings(root):
    if root is None:
        return root
    queue = deque()
    prev = None
    queue.append(root)
    while queue:
        level = len(queue)
        for _ in range(level):
            current = queue.popleft()
            if prev is not None:
                prev.next = current
            prev = current
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

    return root




def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  connect_all_siblings(root)
  root.print_tree()


main()