from tree_node import TreeNode
from collections import deque


def check_completeness(root: TreeNode):
    bfs_queue = deque([root])

    while bfs_queue:
        node = bfs_queue.pop()
        # if the node is non-empty, then keep adding its children
        if node:
            bfs_queue.appendleft(node.left)
            bfs_queue.appendleft(node.right)
        else:
            # once there is an empty node, check if the remaining nodes are also empty.
            while bfs_queue:
                # if not, then return false
                if bfs_queue.pop():
                    return False

    return True
