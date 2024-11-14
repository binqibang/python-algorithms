from typing import Optional

from bt import TreeNode


class Solution:
    def __init__(self):
        self.target = 0
        self.cnt = 1

    def search(self, root, k):
        if not root:
            return
        self.search(root.left, k)
        if self.cnt == k:
            self.target = root.val
        self.cnt += 1
        self.search(root.right, k)

    def kth_smallest(self, root: Optional[TreeNode], k: int) -> int:
        self.search(root, k)
        return self.target
