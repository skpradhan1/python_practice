class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def has_path(root, sum, result):
    if root.left:
        has_path(root.left,sum-root.val,result)
    if root.right:
        has_path(root.right, sum-root.val, result)
    if root.val is sum:
        result.append(True)
    else:
        result.append(False)
    return result


def main():

  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  result = []
  print(has_path(root, 23, result))
  result = []
  print(has_path(root, 16, result))


main()
