"""for better understanding refer FREEFORM"""
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def good_nodes(root: TreeNode):
    def dfs(node, max_val):
        if not node:
            return 0

        total = 1 if node.val >= max_val else 0
        max_val = max(max_val, node.val)

        total += good_nodes(node.left, max_val)
        total += good_nodes(node.right, max_val)

        return total

    return dfs(root, root.val)
