from tree_node import TreeNode
from collections import deque


def bottom_left_value(root: TreeNode):
    bfs_queue = deque([root])

    # create BFS traversal using queue
    while bfs_queue:
        curr_node = bfs_queue.pop()
        # need to add the right subtree first as the last node added will be the leftmost value
        if curr_node.right:
            bfs_queue.appendleft(curr_node.right)
        if curr_node.left:
            bfs_queue.appendleft(curr_node.left)

    # the current node will hold the last popped value so returning the popped value
    return curr_node.val
