"""Check FREEFORM for better understanding"""
# Definition for a binary tree node.
from collections import deque
from tree_node import TreeNode


def right_side_view(root: TreeNode):
    result = []
    bfs_queue = deque()
    bfs_queue.append(root)

    while bfs_queue:
        # for iterating over the queue to remove the parent nodes
        bfs_queue_len = len(bfs_queue)
        right_most_node = None
        for i in range(bfs_queue_len):
            node = bfs_queue.popleft()
            if node:
                # store the last node at every iteration
                right_most_node = node
                bfs_queue.append(node.left)
                bfs_queue.append(node.right)
        if right_most_node:
            result.append(right_most_node.val)
    return result
