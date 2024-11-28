from typing import List


def find_target_sum_ways(nums: List[int], target: int) -> int:
    """
    给你一个非负整数数组 nums 和一个整数 target，向数组中的每个整数前添加 '+' 或 '-' ，
    以使结果数组 nums 的和为 target 。返回符合要求的表达式数目
    :param nums: 整数数组
    :param target: 目标
    :return: 符合要求的表达式数目
    """
    # sum1 - sum2 = target
    # sum1 + sum2 = sum  =>  sum1 = (sum + target) / 2
    total = sum(nums)
    if abs(total) < abs(target):
        return 0
    if (total + target) % 2 != 0:
        return 0
    chosen = (total + target) // 2
    # 问题转化为找到和为chosen子集合数的01背包问题
    dp = [0] * (chosen + 1)
    # 和为0的子集合为空集
    dp[0] = 1
    n = len(nums)
    for i in range(1, n + 1):
        for j in range(chosen, nums[i - 1] - 1, -1):
            dp[j] += dp[j - nums[i - 1]]
    return dp[chosen]


if __name__ == '__main__':
    nums = [1, 1, 1, 1, 1]
    target = 3
    print(find_target_sum_ways(nums, target))
