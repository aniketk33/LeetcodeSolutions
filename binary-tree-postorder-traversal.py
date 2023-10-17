# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


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
