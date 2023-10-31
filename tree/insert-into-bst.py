from tree_node import TreeNode


# recursive solution
def insert_node(root: TreeNode, val):
    # if you reach an empty node
    if not root:
        return TreeNode(val)

    if val > root.val:
        root.right = insert_node(root.right, val)
    else:
        root.left = insert_node(root.left, val)

    return root


# iterative solution
def insert_node_2(root: TreeNode, val):
    # for empty tree
    if not root:
        return TreeNode(val)

    curr_node = root
    while True:
        if val > curr_node.val:
            # if we reach a leaf node
            if not curr_node.right:
                curr_node.right = TreeNode(val)
                return root
            curr_node = curr_node.right
        else:
            # if we reach a leaf node
            if not curr_node.left:
                curr_node.left = TreeNode(val)
                return root
            curr_node = curr_node.left
