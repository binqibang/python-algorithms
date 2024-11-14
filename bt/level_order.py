from typing import List

from bt import TreeNode


def level_order(root: TreeNode) -> List[List[int]]:
    lst = []
    if root is None:
        return lst
    queue = [root]
    while queue:
        n = len(queue)
        level = []
        for i in range(n):
            node = queue.pop(0)
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        lst.append(level)
    return lst
