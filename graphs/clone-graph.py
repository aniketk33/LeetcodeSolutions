# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def clone_graph(node: Node):
    old_new_map = {}

    def dfs(curr_node):
        # return the copy if already present in the dict
        if curr_node in old_new_map:
            return old_new_map[curr_node]

        copy = Node(curr_node.val)
        old_new_map[curr_node] = copy
        for neighbor in curr_node.neighbors:
            # add the neighbors of original node to copy node
            copy.neighbors.append(dfs(neighbor))

        return copy

    # call only when the node is non-empty
    return dfs(node) if node else None
