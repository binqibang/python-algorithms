from typing import List, Optional

from bt import TreeNode


def sorted_array_to_bst(nums: List[int]) -> Optional[TreeNode]:
    """
    将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。
    :param nums: 有序数组
    :return: 二叉搜索树根节点
    """
    def create(start, end):
        if start > end:
            return None
        mid = (start + end) // 2
        root = TreeNode(nums[mid])
        root.left = create(start, mid - 1)
        root.right = create(mid + 1, end)
        return root

    return create(0, len(nums) - 1)


if __name__ == '__main__':
    nums = [-10, -3, 0, 5, 9]
    root = sorted_array_to_bst(nums)
    print(root.val)
