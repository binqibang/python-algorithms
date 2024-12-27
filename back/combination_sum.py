from typing import List


def combination_sum(candidates: List[int], target: int) -> List[List[int]]:
    n = len(candidates)
    stack = []
    ans = []
    candidates.sort()

    def backtrack(i, curr_sum):
        if curr_sum == target:
            ans.append(stack[:])
            return

        for j in range(i, n):
            if candidates[j] <= target - curr_sum:
                stack.append(candidates[j])
                backtrack(j, curr_sum + candidates[j])  # 可以重复选取
                stack.pop()

    backtrack(0, 0)
    return ans


if __name__ == '__main__':
    print(combination_sum([1, 2, 3], 0))
