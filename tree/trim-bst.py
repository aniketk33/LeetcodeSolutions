from tree_node import TreeNode


def trim_bst(root: TreeNode, low, high):
    # empty node
    if not root:
        return None

    # out of bound conditions
    if root.val > high:
        return trim_bst(root.left, low, high)
    if root.val < low:
        return trim_bst(root.right, low, high)

    # if the node is within the range
    root.left = trim_bst(root.left, low, high)
    root.right = trim_bst(root.right, low, high)

    return root
