# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def path_sum(root: TreeNode, target_sum):
    result = []

    def dfs(node, path, remaining_sum):
        if not node:
            return

        # add the current node value to the path
        path.append(node.val)
        # curr_sum += node.val
        if not node.left and not node.right and remaining_sum == node.val:
            # make a new list of given values to store the copy
            result.append(list(path))

        dfs(node.left, path, remaining_sum - node.val)
        dfs(node.right, path, remaining_sum - node.val)
        path.pop()

    dfs(root, [], target_sum)
    return result
