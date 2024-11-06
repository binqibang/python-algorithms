from typing import List


def smallest_range(nums: List[int], k: int) -> int:
    min_val, max_val = min(nums), max(nums)
    if min_val + k >= max_val - k:
        return 0
    else:
        return max_val - min_val - 2 * k


def smallest_range_II(nums: List[int], k: int) -> int:
    nums.sort()
    ans = nums[-1] - nums[0]
    for i in range(len(nums) - 1):
        # 0 -> i add, i + 1 -> -1 sub
        a, b = nums[i], nums[i + 1]
        max_val = max(nums[-1] - k, a + k)
        min_val = min(nums[0] + k, b - k)
        ans = min(ans, max_val - min_val)
    return ans
