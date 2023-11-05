from tree_node import TreeNode


def possible_bt(n):
    # cache the repeated result for performance
    cache = {0: [], 1: [TreeNode()]}

    def backtrack(curr_n):
        if curr_n in cache:
            return cache[curr_n]

        result = []
        for left_tree in range(curr_n):
            # as 1 node will be assigned to the root
            right_tree = (curr_n - 1) - left_tree
            left_sub_tree, right_sub_tree = backtrack(left_tree), backtrack(right_tree)

            for t1 in left_sub_tree:
                for t2 in right_sub_tree:
                    result.append(TreeNode(0, t1, t2))

        cache[curr_n] = result
        return result

    return backtrack(n)
