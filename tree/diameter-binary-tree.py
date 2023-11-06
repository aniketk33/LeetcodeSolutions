# Definition for a binary tree node.
import math
from tree_node import TreeNode


def diameter_binary_tree(root: TreeNode):
    max_diameter = [-math.inf]

    def dfs(root_node: TreeNode):
        if not root_node:
            return -1
        left_node = dfs(root_node.left)
        right_node = dfs(root_node.right)
        diameter = left_node + right_node + 2
        max_diameter[0] = max(max_diameter[0], diameter)

        return 1 + max(left_node, right_node)

    dfs(root)
    return max_diameter[0]
