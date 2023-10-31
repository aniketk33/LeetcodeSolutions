from tree_node import TreeNode


def delete_node(root: TreeNode, val):
    if not root:
        return root

    if val > root.val:
        root.right = delete_node(root.right, val)
    elif val < root.val:
        root.left = delete_node(root.left, val)
    # if val is found
    else:
        # check left node is empty
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
        # find the first min value from the right subtree and replace it with thr given value
        curr_node = root.right
        while curr_node.left:
            curr_node = curr_node.left

        # replace it with the min value
        root.val = curr_node.val
        # recursive call to its child nodes to break the chain
        root.right = delete_node(root.right, root.val)

    return root
