class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None

node = TreeNode(3)
left_node = TreeNode(9)
node.left = left_node
right_node = TreeNode(20)
node.right = right_node
right_node.left = TreeNode(15)
right_node.right = TreeNode(7)

node.right.right = TreeNode(7)

def maxDepth(root):
    if root is None:
        return 0
    left_depth = maxDepth(root.left)
    right_depth = maxDepth(root.right)
    return 1 + max(left_depth, right_depth)

depth = maxDepth(node)
print(depth)


