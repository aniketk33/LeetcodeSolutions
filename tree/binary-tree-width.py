from collections import deque
from tree_node import TreeNode


def width(root: TreeNode):
    # queue with root, num, level
    bfs_queue = deque([[root, 1, 0]])
    result = 0
    prev_num, prev_level = 1, 0

    while bfs_queue:
        node, curr_num, curr_level = bfs_queue.pop()

        # assign the prev level as curr_level's value if it is smaller
        if curr_level > prev_level:
            prev_level = curr_level
            prev_num = curr_num

        result = max(result, curr_num - prev_num + 1)

        if node.left:
            bfs_queue.appendleft([node.left, 2 * curr_num, curr_level + 1])
        if node.right:
            bfs_queue.appendleft([node.right, 2 * curr_num + 1, curr_level + 1])

    return result
