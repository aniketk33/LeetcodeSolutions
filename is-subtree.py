"""refer FREEFORM for better understanding"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_same_tree(p: TreeNode, q: TreeNode):
    if not p and not q:
        return True

    if p and q and p.val == q.val:
        left = is_same_tree(p.left, q.left)
        right = is_same_tree(p.right, q.right)
        return left and right

    return False


def is_sub_tree(root: TreeNode, sub_root: TreeNode):
    # if subtree is empty then it is always true
    if not sub_root:
        return True
    # if parent tree is empty then there cannot be any subtree, so return false
    if not root:
        return False

    # check if both the trees are same
    if is_same_tree(root, sub_root):
        return True

    # recursively iterate over the left and right subtrees
    left = is_sub_tree(root.left, sub_root)
    right = is_sub_tree(root.right, sub_root)

    return left or right
