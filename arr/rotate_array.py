from typing import List


def rotate(nums: List[int], k: int) -> None:
    # 1 2 3 4 5 6 7, k = 3
    # 7 6 5 4 3 2 1 -> 5 6 7 4 3 2 1 -> 5 6 7 1 2 3 4
    def reverse(nums, start, end):
        l, r = start, end
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

    k = k % len(nums)
    reverse(nums, 0, len(nums) - 1)
    reverse(nums, 0, k - 1)
    reverse(nums, k, len(nums) - 1)



