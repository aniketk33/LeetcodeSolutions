from tree_node import TreeNode


def convert_to_bst(num_arr):
    def create_node(left_ptr, right_ptr):
        if left_ptr > right_ptr:
            return None

        # calculate the mid-value and make it as root
        mid_idx = left_ptr + (right_ptr - left_ptr) // 2
        root = TreeNode(num_arr[mid_idx])
        # recursive call on left and right subarray
        root.left = create_node(left_ptr, mid_idx - 1)
        root.right = create_node(mid_idx + 1, right_ptr)

        return root

    return create_node(0, len(num_arr) - 1)
