from tree.tree_node import TreeNode


def tree_path(root: TreeNode):
    result = []
    path = []

    def dfs(curr_node: TreeNode):
        if not curr_node:
            return

        path.append(str(curr_node.val))

        # if both are lead nodes
        if not curr_node.left and not curr_node.right:
            final_path = '->'.join(path)
            result.append(final_path)
        # keep traversing
        else:
            dfs(curr_node.left)
            dfs(curr_node.right)

        # backtrack
        path.pop()

    dfs(root)
    return result


def tree_path_2(root: TreeNode):
    result = []

    def dfs(curr_node: TreeNode, path):
        if not curr_node:
            return

        path += str(curr_node.val)
        # check for leaf nodes
        if not curr_node.left and not curr_node.right:
            result.append(path)
            return

        # traverse the left and right child
        dfs(curr_node.left, path + '->')
        dfs(curr_node.right, path + '->')

    dfs(root, '')
    return result
