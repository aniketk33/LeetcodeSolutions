"""for better understanding refer FREEFORM"""
from tree_node import TreeNode


def good_nodes(root: TreeNode):
    def dfs(node, max_val):
        if not node:
            return 0

        total = 1 if node.val >= max_val else 0
        max_val = max(max_val, node.val)

        total += dfs(node.left, max_val)
        total += dfs(node.right, max_val)

        return total

    return dfs(root, root.val)
