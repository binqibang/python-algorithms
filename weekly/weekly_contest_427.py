from typing import List


class WeeklyContest427:
    def construct_transformed_array(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        for i, num in enumerate(nums):
            j = (i + num) % n
            res[i] = nums[j]

        return res

    def max_subarray_sum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        pre = [0] * (n + 1)
        for i in range(n):
            pre[i + 1] = pre[i] + nums[i]
        print(pre)
        times = 1
        max_sum = -float('inf')
        while times * k <= n:
            step = times * k - 1
            for i in range(0, n - step):
                curr_sum = pre[i + step] - pre[i] + nums[i + step]
                max_sum = max(curr_sum, max_sum)
            times += 1
        return max_sum


if __name__ == '__main__':
    wc = WeeklyContest427()
    print(wc.max_subarray_sum([1, 2], 1))