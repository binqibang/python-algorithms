from typing import List


def permute(nums: List[int], k: int) -> List[List[int]]:
    """
    生成给定整数列表的所有可能的排列组合，每个排列组合的长度为k。
    :param nums: 整数列表
    :param k: 长度
    :return: 所有的排列组合
    """
    perms = []
    lst = []
    n = len(nums)
    visited = [False] * n

    def backtrack(i):
        if i == k:
            perms.append(lst[:])
            return
        for j in range(0, n):
            if not visited[j]:
                lst.append(nums[j])
                visited[j] = True
                backtrack(i + 1)
                visited[j] = False
                lst.pop()

    backtrack(0)
    return perms


if __name__ == '__main__':
    print(permute([1, 2, 3], 2))
