from typing import List


def subarray_sum(nums: List[int], k: int) -> int:
    count, n = 0, len(nums)
    for left in range(n):
        curr_sum = 0
        for right in range(left, n):
            curr_sum += nums[right]
            if curr_sum == k:
                count += 1
    return count


def subarray_sum_ii(nums: List[int], k: int) -> int:
    # [0, i] 子数组和
    count, n = 0, len(nums)
    prefix_map = dict()
    prefix_map[0] = 1
    pre = 0
    for num in nums:
        pre += num
        if pre in prefix_map:
            prefix_map[pre] += 1
        else:
            prefix_map[pre] = 1
    for pre in prefix_map:
        if pre - k in prefix_map:
            count += prefix_map[pre - k]
    return count


def subarray_sum_iii(nums: List[int], k: int) -> int:
    # [0, i] 子数组和
    count, n = 0, len(nums)
    prefix_map = dict()
    prefix_map[0] = 1
    pre = 0
    for num in nums:
        pre += num
        if pre - k in prefix_map:
            count += prefix_map[pre - k]
        if pre in prefix_map:
            prefix_map[pre] += 1
        else:
            prefix_map[pre] = 1
    return count


if __name__ == '__main__':
    nums = [1]
    k = 3
    print(subarray_sum_ii(nums, k))
