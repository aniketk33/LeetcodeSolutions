from collections import defaultdict
from tree_node import TreeNode


def find_duplicate(root: TreeNode):
    result = []
    serializer_dict = defaultdict(list)

    def dfs(curr_node: TreeNode):
        # append None to the serialized string if there is no child
        if not curr_node:
            return 'None'
        # traverse in pre order: Root, left, right
        serialized_str = ','.join([str(curr_node.val), dfs(curr_node.left), dfs(curr_node.right)])
        # if there exist a similar pattern in the dict, then append it to the result
        if len(serializer_dict[serialized_str]) == 1:
            result.append(curr_node)

        serializer_dict[serialized_str].append(curr_node)

        return serialized_str

    dfs(root)
    return result
