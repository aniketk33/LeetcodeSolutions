from tree_node import TreeNode


def is_same_tree(p: TreeNode, q: TreeNode):
    # check if both are empty or not
    if not p and not q:
        return True
    # check if either of them is empty or with different value
    if not p or not q or p.val != q.val:
        return False

    # recursive call to left and right subtrees of both the given trees
    left = is_same_tree(p.left, q.left)
    right = is_same_tree(p.right, q.right)
    return left and right
