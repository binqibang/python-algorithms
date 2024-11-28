from typing import Optional

from bt import TreeNode


def path_sum(root: Optional[TreeNode], targetSum: int) -> int:
    """
    计算二叉树中所有路径的和等于给定值的路径数量。

    :param root: TreeNode类型，二叉树的根节点。
    :param targetSum: int类型，目标和。
    :return int类型，满足路径和等于targetSum的路径数量。
    """

    # 定义一个内部函数count，用于计算从当前节点开始的路径中，有多少条路径的和等于目标值
    def count(root: Optional[TreeNode], target: int):
        if not root:
            return 0
        ret = 0
        if root.val == target:
            ret += 1
        target -= root.val
        ret += count(root.left, target)
        ret += count(root.right, target)
        return ret

    # 先序遍历所有节点
    if not root:
        return 0
    ans = count(root, targetSum)
    ans += path_sum(root.left, targetSum)
    ans += path_sum(root.right, targetSum)
    return ans
