from typing import List


def daily_temperatures(temperatures: List[int]) -> List[int]:
    # 73,74,75,71,69,72,76,73
    # 1, 1, 4, 2, 1, 1, 0, 0
    n = len(temperatures)
    ans = [0] * n
    stack = []
    for i in range(n):
        while len(stack) > 0 and temperatures[i] > temperatures[stack[-1]]:
            pre = stack.pop()
            ans[pre] = i - pre
        stack.append(i)
    return ans


if __name__ == '__main__':
    print(daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]))
