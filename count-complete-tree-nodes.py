# Definition for a binary tree node.
import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def left_tree_height(node: TreeNode):
    if not node:
        return 0
    return left_tree_height(node.left + 1)


def right_tree_height(node: TreeNode):
    if not node:
        return 0
    return right_tree_height(node.right + 1)


def count_nodes(root: TreeNode):
    if not root:
        return 0
    left_height = left_tree_height(root)
    right_height = right_tree_height(root)

    if left_height == right_height:
        return int(math.pow(2, left_height) - 1)

    return count_nodes(root.left) + count_nodes(root.right) + 1
