"""Given the root of a binary search tree and an integer k, return true if there exist two elements in the BST such
that their sum is equal to k, or false otherwise"""
from tree_node import TreeNode


def find_target(root: TreeNode, target):
    # add the differences as you traverse the tree
    differences = set()

    def dfs(curr_node: TreeNode):
        if not curr_node:
            return
        # check if the difference node is present in the set
        diff = target - curr_node.val
        if diff in differences:
            return True
        else:
            # if not, then add the current node's val to the set
            differences.add(curr_node.val)

        # traverse left and right subtrees
        return dfs(curr_node.left) or dfs(curr_node.right)

    return dfs(root)
