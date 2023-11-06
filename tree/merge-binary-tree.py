from tree_node import TreeNode


def merge_tree(left_tree: TreeNode, right_tree: TreeNode):
    if not left_tree and not right_tree:
        return None
    # get the left and right value of the node
    left_val = left_tree.val if left_tree else 0
    right_val = right_tree.val if right_tree else 0

    root = TreeNode(left_val + right_val)
    # if a left or right tree is None, it will cause an error while accessing the left_tree's or right_tree's left and
    # right tree respectively, so pass in None
    root.left = merge_tree(left_tree.left if left_tree else None, right_tree.left if right_tree else None)
    root.right = merge_tree(left_tree.right if left_tree else None, right_tree.right if right_tree else None)

    return root
