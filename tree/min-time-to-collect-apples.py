def min_time(n, edges, has_apples):
    # create adjacent hashmap for nodes
    adjacent_nodes = {i: [] for i in range(n)}
    for parent, child in edges:
        adjacent_nodes[parent].append(child)
        adjacent_nodes[child].append(parent)

    def dfs(curr_node, parent_node):
        time = 0
        for child_node in adjacent_nodes[curr_node]:
            # do not want to loop back again to the parent
            if child_node == parent_node:
                continue

            child_time = dfs(child_node, curr_node)
            if child_time or has_apples[child_node]:
                # the back and forth traversal takes 2 units of time, hence adding 2
                time += 2 + child_time

        return time

    return dfs(0, -1)


nodes = 7
e = [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]]
hasApple = [False, False, True, False, True, True, False]
res = min_time(nodes, e, hasApple)
print(res)
