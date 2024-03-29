# Definition for a binary tree node.
from typing import List
from tree_node import TreeNode


def build_tree(preorder: List[int], inorder: List[int]):
    if not preorder or not inorder:
        return None

    # preorder's first value is always the root value
    root_val = preorder[0]
    root = TreeNode(root_val)
    # choose the mid-index from the inorder list as the left side of the mid-index is
    # a left tree and the right side is the right tree
    mid = inorder.index(root_val)
    # construct the left and right side of the tree
    root.left = build_tree(preorder[1:mid + 1], inorder[:mid])
    root.right = build_tree(preorder[mid + 1:], inorder[mid + 1:])

    return root
