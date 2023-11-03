def unique_bst(n):
    num_trees = [1] * (n + 1)

    # why start from 2? because values for 0 and 1 nodes are 1. that is why the initialization of array was with 1s
    for nodes in range(2, n + 1):
        # calculate the sum at each subtree formation
        total = 0
        for root in range(1, nodes + 1):
            left_tree = root - 1
            right_tree = nodes - root
            total += num_trees[left_tree] * num_trees[right_tree]

        # update the value for the particular number nodes
        num_trees[nodes] = total

    return num_trees[n]


res = unique_bst(4)
print(res)
