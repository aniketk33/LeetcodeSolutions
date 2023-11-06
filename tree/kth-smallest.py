from tree_node import TreeNode


def kth_smallest(root: TreeNode, k: int):
    n = 0
    stack = []
    curr = root

    # loop until stack is non-empty and node is not none
    while curr and stack:
        # iteratively loop to the leftmost child
        while curr:
            stack.append(curr)
            curr = curr.left

        # pop the left child before going a step back to the root
        curr = stack.pop()
        n += 1
        if n == k:
            return curr.val

        # now visit the right child
        curr = curr.right


def kth_smallest_2(root: TreeNode, k: int):
    """recursive solution"""
    inorder_traversal = []

    def dfs(node):
        if not node:
            return

        dfs(node.left)
        inorder_traversal.append(node.val)
        dfs(node.right)

    dfs(root)
    return inorder_traversal[k - 1]
