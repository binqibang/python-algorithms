from collections import Counter
from typing import List


class WeeklyContest423:
    def has_increasing_subarrays(self, nums: List[int], k: int) -> bool:
        def is_increasing(arr: List[int]) -> bool:
            for i in range(len(arr) - 1):
                if arr[i] >= arr[i + 1]:
                    return False
            return True

        for i in range(len(nums) - k * 2 + 1):
            if (is_increasing(nums[i: i + k]) and
                    is_increasing(nums[i + k: i + k * 2])):
                return True
        return False

    def max_increasing_subarrays(self, nums: List[int]) -> int:
        max_k, n = 0, len(nums)

        # 初始化后缀数组，用于记录从每个元素开始的递增子数组长度
        start = [1] * n
        # 从后向前遍历，填充后缀数组
        for i in range(n - 1, -1, -1):
            # 如果当前元素小于下一个元素，说明是递增的
            if i < n - 1 and nums[i] < nums[i + 1]:
                # 当前元素所在的递增子数组长度为下一个元素的长度加1
                start[i] = start[i + 1] + 1

        # 初始化前缀数组，用于记录到每个元素结束的递增子数组长度
        end = [1] * n
        # 从前向后遍历，填充前缀数组
        for i in range(n):
            # 如果当前元素大于前一个元素，说明是递增的
            if i > 0 and nums[i] > nums[i - 1]:
                # 当前元素所在的递增子数组长度为前一个元素的长度加1
                end[i] = end[i - 1] + 1
            # 如果不是最后一个元素，更新最大长度
            if i < n - 1:
                max_k = max(max_k, min(end[i], start[i + 1]))

        # 返回最大长度
        return max_k

    def sum_of_good_subsequences(self, nums: List[int]) -> int:
        mod = int(1e9 + 7)

        count = Counter()       # 末尾为count[i]的好子序列个数
        subseq_sum = Counter()  # 末尾为count[i]的好子序列和
        ans = 0

        for num in nums:
            curr_sum = num
            # 与所有末尾为num+1成为好子序列
            curr_sum += num * count[num + 1] + count[num - 1]
            # 与所有末尾为num-1成为好子序列
            curr_sum += num * count[num - 1] + count[num + 1]

            count[num] += 1 + count[num + 1] + count[num - 1]
            count[num] %= mod
            subseq_sum[num] = (curr_sum + subseq_sum[num]) % mod
            ans = (ans + curr_sum) % mod

        return ans


if __name__ == '__main__':
    wc = WeeklyContest423()
    # print(list(range(9 - 3)))
    nums = [2, 5, 7, 8, 9, 2, 3, 4, 3, 1]
    k = 2
    wc.max_increasing_subarrays(nums)
