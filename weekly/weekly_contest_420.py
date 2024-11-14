import math
from typing import List


class WeeklyContest420:
    def string_sequence(self, target: str) -> List[str]:
        ans = []
        curr = []
        for i, ch in enumerate(target):
            curr.append('a')
            ans.append("".join(curr))
            for j in range(ord(ch) - ord('a')):
                curr[i] = chr(ord('a') + j + 1)
                ans.append("".join(curr))
        return ans

    def number_of_substrings(self, s: str, k: int) -> int:
        ans = 0
        n = len(s)
        for left in range(n):
            count = dict()
            for right in range(left, n):
                if s[right] in count:
                    count[s[right]] += 1
                else:
                    count[s[right]] = 1
                if count[s[right]] >= k:
                    ans += n - right
                    break
        return ans

    def min_operations(self, nums: List[int]) -> int:
        # 获取x最大真因数
        def find_factor(x):
            if x <= 1:
                return 1
            for i in range(2, int(math.sqrt(x)) + 1, 1):
                if x % i == 0:
                    if i * i == x:
                        return i
                    else:
                        return x // i
            return 1

        cnt = 0
        prev = nums[-1]
        # 从后往前遍历
        for i in range(len(nums) - 2, -1, -1):
            # 满足非递减
            if nums[i] <= prev:
                prev = nums[i]
            else:
                factor = find_factor(nums[i])
                if nums[i] / factor > prev:
                    return -1
                prev = nums[i] / factor
                cnt += 1
        return cnt


if __name__ == '__main__':
    wc420 = WeeklyContest420()
    target = "abc"
    print(wc420.string_sequence(target))
    s, k = "abcab", 2
    print(wc420.number_of_substrings(s, k))
    nums = [25, 7]
    print(wc420.min_operations(nums))
