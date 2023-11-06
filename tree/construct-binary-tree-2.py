from typing import List
from tree_node import TreeNode


def construct_tree(inorder: List[int], postorder: List[int]):
    if not inorder:
        return None

    # the last node of post-order is the root
    root = TreeNode(postorder.pop())

    mid_idx = inorder.index(root.val)
    root.right = construct_tree(inorder[mid_idx + 1:], postorder)
    root.left = construct_tree(inorder[:mid_idx], postorder)

    return root


# efficient solution as it prevents creating a subarray and also, traversal to find the mid-index
def construct_tree_2(inorder: List[int], postorder: List[int]):
    index_dict = {val: idx for idx, val in enumerate(inorder)}

    def create_tree(left_ptr, right_ptr):
        if left_ptr > right_ptr:
            return None

        root = TreeNode(postorder.pop())
        mid_idx = index_dict[root.val]
        root.right = create_tree(mid_idx + 1, right_ptr)
        root.left = create_tree(left_ptr, mid_idx - 1)

        return root

    return create_tree(0, len(inorder) - 1)
