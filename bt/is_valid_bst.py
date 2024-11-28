from bt import TreeNode


def is_valid_bst(root: TreeNode) -> bool:

    def dfs(root: TreeNode, prev_val):
        if not root:
            return True
        if not dfs(root.left, prev_val):
            return False

        if prev_val >= root.val:
            return False
        prev_val = root.val

        return dfs(root.right, prev_val)

    return dfs(root, -float('inf'))
