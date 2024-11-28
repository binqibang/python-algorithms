from typing import Optional

from bt import TreeNode


class Solution:

    def __init__(self):
        self.prev = None

    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root:
            return
        if self.prev:
            self.prev.left = None
            self.prev.right = root
        self.prev = root
        right = root.right
        self.flatten(root.left)
        self.flatten(right)
