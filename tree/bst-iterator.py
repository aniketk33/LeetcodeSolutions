from typing import Optional
from tree_node import TreeNode


class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.dfs_stack = []
        # add the nodes till the last left value
        while root:
            self.dfs_stack.append(root)
            root = root.left

    def next(self) -> int:
        # pop the last value and add all its right child
        next_value = self.dfs_stack.pop()
        curr_node = next_value.right
        while curr_node:
            self.dfs_stack.append(curr_node)
            curr_node = curr_node.left

        return next_value.val

    def hasNext(self) -> bool:
        # check if stack is non-empty
        return self.dfs_stack != []

# Your BSTIterator object will be instantiated, and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
