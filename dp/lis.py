from typing import List


def lengthOfLIS(nums: List[int]) -> int:
    # 10, 9, 2, 5, 3, 7, 101, 18
    # 2 5 7 18
    n = len(nums)
    dp = [1] * n
    max_len = dp[0]
    for i in range(1, n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
        max_len = max(max_len, dp[i])
    return max_len