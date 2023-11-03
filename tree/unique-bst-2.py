"""return the unique combinations of a formed bst tree"""
from tree_node import TreeNode


def unique_bst(n):
    def generate_trees(left_ptr, right_ptr):
        # if the root does not have any right or left child
        if left_ptr > right_ptr:
            return [None]

        result = []
        for val in range(left_ptr, right_ptr + 1):
            # generate left and right subtrees for the given range
            for left_tree in generate_trees(left_ptr, val - 1):
                for right_tree in generate_trees(val + 1, right_ptr):
                    root = TreeNode(val, left_tree, right_tree)
                    result.append(root)

        return result

    return generate_trees(left_ptr=1, right_ptr=n)


# much efficient solution than above as it uses dynamic programming to store preliminary results
def unique_bst_2(n):
    dp = {}

    def generate_trees(left_ptr, right_ptr):
        # if the root does not have any right or left child
        if left_ptr > right_ptr:
            return [None]

        if (left_ptr, right_ptr) in dp:
            return dp[(left_ptr, right_ptr)]

        result = []
        for val in range(left_ptr, right_ptr + 1):
            # generate left and right subtrees for the given range
            for left_tree in generate_trees(left_ptr, val - 1):
                for right_tree in generate_trees(val + 1, right_ptr):
                    root = TreeNode(val, left_tree, right_tree)
                    result.append(root)

        dp[(left_ptr, right_ptr)] = result
        return result

    return generate_trees(left_ptr=1, right_ptr=n)
