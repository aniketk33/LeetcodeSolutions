from tree_node import TreeNode


def convert_bst(root: TreeNode):
    curr_sum = 0

    def dfs(curr_node: TreeNode):
        if not curr_node:
            return

        # reverse inorder traversal starting from right
        dfs(curr_node.right)

        # calculate the curr_sum and update the curr_node val
        nonlocal curr_sum
        temp = curr_node.val
        curr_node.val += curr_sum
        curr_sum += temp

        dfs(curr_node.left)

    dfs(root)
    return root
