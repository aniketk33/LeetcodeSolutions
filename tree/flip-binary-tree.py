from tree_node import TreeNode


def flip_tree(root1: TreeNode, root2: TreeNode):
    # base cases
    # return False if either one of them is empty
    if not root1 or not root2:
        # return True if both are empty
        if not root1 and not root2:
            return True
        return False

    # return false is the values are not equal
    if root1.val != root2.val:
        return False

    # same trees
    same_tree_result = flip_tree(root1.left, root2.left) and flip_tree(root1.right, root2.right)
    # after flipping
    flip_tree_result = flip_tree(root1.left, root2.right) and flip_tree(root1.right, root2.left)

    return same_tree_result or flip_tree_result
