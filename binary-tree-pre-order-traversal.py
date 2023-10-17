"""refer FREEFORM for better understanding"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preorder_traversal(root: TreeNode):
    dfs_stack = []
    result = []
    curr_node = root

    while dfs_stack or curr_node:
        if curr_node:
            result.append(curr_node.val)
            dfs_stack.append(curr_node.right)
            curr_node = curr_node.left
        else:
            curr_node = dfs_stack.pop()

    return result
