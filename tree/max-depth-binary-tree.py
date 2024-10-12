def max_depth(root):
    def dfs(node):
        if not node:
            return 0

        left = dfs(node.left)
        right = dfs(node.right)

        return 1 + (left if left > right else right)

    return dfs(root)


# iterative solution
def max_depth_2(root):
    # for empty node
    if not root:
        return 0

    stack = [(root, 0)]
    max_depth = 0

    while stack:
        curr_node, curr_depth = stack.pop()
        # as None child is also added to the stack, so taking care of None value
        if curr_node:
            if curr_depth > max_depth:
                max_depth = curr_depth
            # add both children of current node and explore
            stack.append((curr_node.left, curr_depth + 1))
            stack.append((curr_node.right, curr_depth + 1))

    return max_depth + 1
