# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorder_traversal(root: TreeNode):
    """using stack data structure as we are doing depth first search (dfs)"""
    dfs_stack = []
    result = []
    curr_node = root

    while curr_node or dfs_stack:
        while curr_node:
            dfs_stack.append(curr_node)
            curr_node = curr_node.left

        curr_node = dfs_stack.pop()
        result.append(curr_node.val)
        curr_node = curr_node.right

    return result
