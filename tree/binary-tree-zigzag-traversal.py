from collections import deque

from tree_node import TreeNode


def zigzag_traversal(root: TreeNode):
    result = []
    bfs_queue = deque([root] if root else [])

    while bfs_queue:
        curr_level = []
        for _ in range(len(bfs_queue)):
            curr_node = bfs_queue.popleft()
            curr_level.append(curr_node.val)
            if curr_node.left:
                bfs_queue.append(curr_node.left)
            if curr_node.right:
                bfs_queue.append(curr_node.right)

        # reverse the order for odd index. why before adding?
        # because if the level is going to be added to an odd position, therefore check before adding and not after!!
        curr_level = curr_level[::-1] if len(result) % 2 == 1 else curr_level
        result.append(curr_level)

    return result
