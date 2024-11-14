from typing import List


def can_partition(nums: List[int]) -> bool:
    n = len(nums)
    if n < 2:
        return False

    total, max_num = sum(nums), max(nums)
    if total % 2 != 0:
        return False

    target = total / 2
    if target < max_num:
        return False

    # dp[i][j]: 从数组的 [0,i] 下标范围内选取若干个正整数（可以是 0 个），
    # 是否存在一种选取方案使得被选取的正整数的和等于 j
    dp = [[False] * (target + 1) for _ in range(n + 1)]
    # 不选取任何正整数，则被选取的正整数之和等于 0，因此 0≤i<n，dp[i][0] = true
    for i in range(n + 1):
        dp[i][0] = True

    for i in range(1, n + 1):
        for j in range(1, target + 1):
            # 如果 j≥nums[i]，则对于当前的数字 nums[i]，可以选取也可以不选取。
            # 如果不选取 nums[i]，则 dp[i][j]=dp[i−1][j]；
            # 如果选取 nums[i]，则 dp[i][j]=dp[i−1][j−nums[i]]。
            if nums[i - 1] <= j:
                dp[i][j] = dp[i - 1][j] | dp[i - 1][j - nums[i - 1]]
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[n][target]


def can_partition_ii(nums: List[int]) -> bool:
    n = len(nums)
    if n < 2:
        return False

    total, max_num = sum(nums), max(nums)
    if total % 2 != 0:
        return False

    target = total / 2
    if target < max_num:
        return False

    dp = [True] + [False] * target

    for i in range(1, n + 1):
        for j in range(target, nums[i - 1] - 1, -1):
            dp[j] = dp[j] | dp[j - nums[i - 1]]

    return dp[target]
