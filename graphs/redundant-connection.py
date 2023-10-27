def redundant_connection(edges):
    # edges start from 1, so 0th index will not be in use
    parent_arr = [i for i in range(len(edges) + 1)]
    rank_arr = [1] * (len(edges) + 1)

    # find parent of the given node
    def find_parent(node):
        p = parent_arr[node]
        # loop to find the root parent of the given node
        while parent_arr[p] != p:
            # jumping two steps backward
            parent_arr[p] = parent_arr[parent_arr[p]]
            # assign the new parent
            p = parent_arr[p]

        return p

    def union(node_1, node_2):
        parent_1, parent_2 = find_parent(node_1), find_parent(node_2)

        # if cycle is detected return false
        if parent_1 == parent_2:
            return False

        # compare the rank of each parent of given two nodes
        if rank_arr[parent_1] > rank_arr[parent_2]:
            # assign the latest parent
            parent_arr[parent_2] = parent_1
            # increment the rank of the parent
            rank_arr[parent_1] += rank_arr[parent_2]
        else:
            parent_arr[parent_1] = parent_2
            rank_arr[parent_2] += rank_arr[parent_1]

        return True

    for n1, n2 in edges:
        if not union(n1, n2):
            return [n1, n2]


e = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]
res = redundant_connection(e)
print(res)
