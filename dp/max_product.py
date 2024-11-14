from typing import List


def max_product(nums: List[int]) -> int:
    n = len(nums)

    dp_max = nums[:]  # 以nums[i]结尾最大子数组和
    dp_min = nums[:]  # 以nums[i]结尾最小子数组和

    for i in range(1, n):
        dp_max[i] = max(dp_max[i], dp_max[i - 1] * nums[i], dp_min[i - 1] * nums[i])
        dp_min[i] = min(dp_min[i], dp_max[i - 1] * nums[i], dp_min[i - 1] * nums[i])

    ans = -float('inf')
    for e in dp_max:
        ans = max(e, ans)

    return ans


if __name__ == '__main__':
    nums = [2, 3, -2, 4]
    max_product(nums)
