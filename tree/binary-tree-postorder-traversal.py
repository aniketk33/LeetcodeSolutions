from tree_node import TreeNode


def postorder_traversal(root: TreeNode):
    """refer FREEFORM for better understanding"""
    stack = [(root, False)]
    result = []
    while stack:
        curr_node, visited = stack.pop()
        if curr_node:
            if visited:
                result.append(curr_node.val)
            else:
                # append the root and value as True because we are going to explore its child
                stack.append((curr_node, True))
                # add their children
                stack.append((curr_node.right, False))
                stack.append((curr_node.left, False))

    return result
