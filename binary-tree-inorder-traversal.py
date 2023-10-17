# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorder_traversal(root: TreeNode):
    """using stack data structure"""
    bfs_stack = []
    result = []
    curr_node = root

    while curr_node or bfs_stack:
        while curr_node:
            bfs_stack.append(curr_node)
            curr_node = curr_node.left

        curr_node = bfs_stack.pop()
        result.append(curr_node.val)
        curr_node = curr_node.right

    return result
