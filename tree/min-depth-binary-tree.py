# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def min_depth(root: TreeNode):
    if not root:
        return 0

    depth = [float('inf')]

    def dfs(node, curr_depth):
        if not node:
            return

        if not node.left and not node.right:
            depth[0] = min(depth[0], curr_depth)

        dfs(node.left, curr_depth + 1)
        dfs(node.right, curr_depth + 1)

    dfs(root, 1)
    return depth[0]
