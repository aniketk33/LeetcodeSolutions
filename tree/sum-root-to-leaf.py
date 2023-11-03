from tree_node import TreeNode


def sum_root(root: TreeNode):
    def dfs(curr_node: TreeNode, curr_sum: int):
        if not curr_node:
            return 0

        # calculate the sum
        curr_sum = curr_sum * 10 + curr_node.val

        # check if it is a leaf node
        if not curr_node.left and not curr_node.right:
            return curr_sum

        # traverse left and right subtree
        return dfs(curr_node.left, curr_sum) + dfs(curr_node.right, curr_sum)

    return dfs(root, 0)
