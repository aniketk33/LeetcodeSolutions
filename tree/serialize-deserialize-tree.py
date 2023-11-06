# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from tree_node import TreeNode


class Codec:

    def __init__(self):
        self.curr_idx = 0

    def serialize(self, root: TreeNode):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        result = []

        def dfs(curr_node: TreeNode):
            if not curr_node:
                result.append('N')
                return
            # pre-order traversal

            # append the root node
            result.append(str(curr_node.val))
            dfs(curr_node.left)
            dfs(curr_node.right)

        dfs(root)
        return ','.join(result)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        tree_nodes = data.split(',')
        self.curr_idx = 0

        def dfs():
            if tree_nodes[self.curr_idx] == 'N':
                self.curr_idx += 1
                return None
            node = TreeNode(tree_nodes[self.curr_idx])
            self.curr_idx += 1
            node.left = dfs()
            node.right = dfs()

            return node

        return dfs()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
