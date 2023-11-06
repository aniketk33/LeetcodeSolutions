from tree_node import TreeNode


def path_sum(root: TreeNode, target_sum):
    def dfs(node, curr_sum):
        # check a base case
        if not node:
            return False

        # calculate current sum
        curr_sum += node.val

        # if it is a leaf node, then check whether the curr and target sum are same
        if not node.left and not node.right:
            return curr_sum == target_sum

        return dfs(node.left, curr_sum) or dfs(node.right, curr_sum)

    return dfs(root, 0)
