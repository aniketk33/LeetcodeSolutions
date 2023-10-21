# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def level_order_traversal(root: TreeNode):
    result = []
    bfs_queue = collections.deque()
    # add the root node
    bfs_queue.append(root)

    while bfs_queue:
        bfs_queue_len = len(bfs_queue)
        temp_result = []
        for i in range(bfs_queue_len):
            node = bfs_queue.popleft()
            if node:
                temp_result.append(node.val)
                # add its children to the queue
                bfs_queue.append(node.left)
                bfs_queue.append(node.right)
        # do not include not empty nodes
        if temp_result:
            result.append(temp_result)

    return result
