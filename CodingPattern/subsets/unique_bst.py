class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None


def find_unique_trees(n):
  if n <= 0:
    return []
  return findUnique_trees_recursive(1, n)

def findUnique_trees_recursive(start, end):
    result = []

    if start > end:
        result.append(None)
        return result

    for i in range(start, end+1):
        leftSubtree = findUnique_trees_recursive(start, i-1)
        rightSubtree = findUnique_trees_recursive(i+1, end)
        for left in leftSubtree:
            for right in rightSubtree:
                root = TreeNode(i)
                root.left = left
                root.right = right
                result.append(root)
    return result


print("Total trees: " + str(find_unique_trees(3)))


