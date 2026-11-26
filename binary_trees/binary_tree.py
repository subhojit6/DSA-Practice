class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

node = TreeNode(8)
left_node = TreeNode(3)
node.left = left_node
left_node.right = TreeNode(6)
right_node = TreeNode(12)
node.right = right_node

def preorder(current):
    if current is None:
        return
    print(current.value)
    preorder(current.left)
    preorder(current.right)

def inorder(current):
    if current is None:
        return
    inorder(current.left)
    print(current.value)
    print(current.right)

def postorder(current):
    if current is None:
        return
    postorder(current.left)
    postorder(current.right)
    print(current.value)




