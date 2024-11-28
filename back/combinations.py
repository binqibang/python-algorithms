from typing import List


def combine(nums: List[int], k: int) -> List[List[int]]:
    """
    从nums中选取k个数组合
    :param nums: 列表
    :param k: 选取的个数
    :return: 所有的组合
    """
    n = len(nums)
    combs = []
    stack = []

    def backtrack(i: int):
        if len(stack) == k:
            combs.append(stack[:])
            return
        for j in range(i, n):
            stack.append(nums[j])
            backtrack(j + 1)
            stack.pop()

    backtrack(0)
    return combs


if __name__ == '__main__':
    print(combine([1, 2, 3, 4, 8], 3))
