from tree_node import TreeNode


def min_distance(root: TreeNode):
    prev_node, result = None, float('inf')

    def dfs(curr_node: TreeNode):
        if not curr_node:
            return
        # INORDER TRAVERSAL
        # recursive call to left subtree
        dfs(curr_node.left)
        # to access the global variable
        nonlocal result, prev_node

        # calculate the difference between the two nodes
        if prev_node:
            result = min(result, curr_node.val - prev_node.val)

        # assign the current node as prev_node
        prev_node = curr_node
        # recursive call to right subtree
        dfs(curr_node.right)

    dfs(root)
    return result
