class TreeNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def create_bt(preorder: list[int], inorder: list[int]) -> TreeNode:
    # pre 3 9 20 15 7
    # in  9 3 15 20 7
    def build(pre_start, pre_end, in_start, in_end):
        if pre_start > pre_end:
            return None
        root_val = preorder[pre_start]
        root = TreeNode(root_val)
        root_idx = inorder.index(root_val)
        left_len = root_idx - in_start
        root.left = build(pre_start + 1, pre_start + left_len, in_start, root_idx - 1)
        root.right = build(pre_start + left_len + 1, pre_end, root_idx + 1, in_end)
        return root

    return build(0, len(preorder) - 1, 0, len(inorder) - 1)
