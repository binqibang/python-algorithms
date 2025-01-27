from typing import List


class WeeklyContest424:
    def count_valid_selections(self, nums: List[int]) -> int:
        n = len(nums)
        # [0, i - 1] 数组元素和
        prefix = [0] * n
        for i in range(1, n):
            prefix[i] = prefix[i - 1] + nums[i - 1]
        # [i + 1, n - 1] 数组元素和
        suffix = [0] * n
        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] + nums[i + 1]

        cnt = 0
        for i in range(n):
            if nums[i] == 0:
                if prefix[i] == suffix[i]:
                    cnt += 2
                if abs(prefix[i] - suffix[i]) == 1:
                    cnt += 1
        return cnt

    def is_zero_array(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        diff = [0] * n
        for l, r in queries:
            diff[l] += 1
            if r + 1 < n:
                diff[r + 1] -= 1
        curr = 0
        for i in range(n):
            curr += diff[i]
            if curr < nums[i]:
                return False
        return True

    def min_zero_array(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)

        def check(pos):
            diff = [0] * n
            for i in range(pos):
                l, r, val = queries[i]
                diff[l] += val
                if r + 1 < n:
                    diff[r + 1] -= val
            curr = 0
            for i in range(n):
                curr += diff
                if curr < nums[i]:
                    return False
            return True

        start, end = 0, len(queries)
        res = -1
        while start <= end:
            mid = (start + end) // 2
            if check(mid):
                res = mid
                end = mid - 1
            else:
                start = mid + 1

        return res


if __name__ == '__main__':
    wc = WeeklyContest424()
    print(wc.count_valid_selections([16, 13, 10, 0, 0, 0, 10, 6, 7, 8, 7]))
