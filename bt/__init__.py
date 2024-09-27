class BTNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def create_bt(preorder: list[int], inorder: list[int]) -> BTNode:
    # pre 3 9 20 15 7
    # in  9 3 15 20 7
    def build(preorder, p_start, p_end, inorder, i_start, i_end):
        if p_start > p_end or i_start > i_end:
            return None
        root_val = preorder[p_start]
        root = BTNode(root_val)
        root_idx = inorder.index(root_val)
        left_len = root_idx - i_start
        root.left = build(preorder, p_start + 1, p_start + left_len,
                          inorder, i_start, root_idx - 1)
        root.right = build(preorder, p_start + left_len + 1, p_end,
                           inorder, root_idx + 1, i_end)
        return root

    return build(preorder, 0, len(preorder) - 1, inorder, 0, len(inorder) - 1)
