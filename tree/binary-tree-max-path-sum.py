from tree_node import TreeNode


def max_sum(root: TreeNode):
    result = root.val

    # return the max value without splitting
    def dfs(curr_node: TreeNode):
        # base case
        if not curr_node:
            return 0

        # calculate left and right subtree's max value
        left_tree = dfs(curr_node.left)
        right_tree = dfs(curr_node.right)
        left_tree = max(left_tree, 0)
        right_tree = max(right_tree, 0)

        nonlocal result
        # split the nodes of the path and calculate the max
        result = max(result, curr_node.val + left_tree + right_tree)

        # return the max value without splitting
        return curr_node.val + max(left_tree, right_tree)

    dfs(root)
    return result
