from typing import Optional

from bt import TreeNode


class Solution:
    def __init__(self):
        self.max_sum = -float('inf')

    def max_path_sum(self, root: Optional[TreeNode]) -> int:
        def dfs(root: Optional[TreeNode]):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            self.max_sum = max(self.max_sum, left + right)
            return left + right + root.val

        dfs(root)
        return self.max_sum
