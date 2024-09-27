from typing import List


def getSneakyNumbers(nums: List[int]) -> List[int]:
    cnt = {}
    for num in nums:
        if num in cnt:
            cnt[num] += 1
        else:
            cnt[num] = 1
    ans = []
    for k, v in cnt.items():
        if v == 2:
            ans.append(k)
    return ans

