from typing import List


def subsets(nums: List[int]) -> List[List[int]]:
    n = len(nums)
    ans = []
    stack = []

    def backtrack(i):
        ans.append(stack[:])
        for j in range(i, n):
            stack.append(nums[j])
            backtrack(j + 1)
            stack.pop()

    backtrack(0)
    return ans


if __name__ == '__main__':
    print(subsets([1, 2, 3]))
