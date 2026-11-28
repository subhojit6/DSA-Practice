from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

node = TreeNode(8)
left_node = TreeNode(3)
node.left = left_node
left_node.right = TreeNode(6)
right_node = TreeNode(12)
node.right = right_node

if node is None:
    print("[]")
else:
    queue = deque([node])
    result = []

    while queue:
        level_size = len(queue)
        current_level = []
        for _ in range(level_size):
            value = queue.popleft()
            current_level.append(value.val)
            if value.left:
                queue.append(value.left)
            if value.right:
                queue.append(value.right)

        result.append(current_level)
    print(result)