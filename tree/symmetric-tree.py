# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def symmetric_tree(root: TreeNode):
    def dfs(left_node, right_node):
        # Tree is symmetric if both the nodes are empty
        if not left_node and not right_node:
            return True
        # and it not when either of them are empty
        if not left_node or not right_node:
            return False

        # check for their value, and recursively call left node's left child and right node's right child
        # and vice versa
        return (left_node.val == right_node.val and
                dfs(left_node.left, right_node.right) and
                dfs(left_node.right, right_node.left))

    return dfs(root.left, root.right)
