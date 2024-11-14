from bt import TreeNode


class Solution(object):

    def __init__(self):
        self.diameter = 0

    def diameter_of_bt(self, root: TreeNode) -> int:
        def dfs(root: TreeNode) -> int:
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            self.diameter = max(self.diameter, left + right)
            return 1 + max(left, right)

        dfs(root)
        return self.diameter
