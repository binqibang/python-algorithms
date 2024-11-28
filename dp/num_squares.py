import math


def num_squares(n: int) -> int:
    """
    给定正整数n，返回完全平方数的最少数量，完全平方数是平方数之和，例如1，4，9，16等。
    :param n: 目标值
    :return: 最少数量
    """
    # dp[i]: 和为i的完全平方数最小数量
    dp = [float('inf')] * (n + 1)
    dp[0] = 0

    squares = []
    for i in range(1,  int(math.sqrt(n)) + 1):
        squares.append(i * i)
    print(squares)

    for i in range(0, len(squares)):
        for j in range(squares[i], n + 1):
            dp[j] = min(dp[j], dp[j - squares[i]] + 1)

    print(dp[n])
    return dp[n]


if __name__ == '__main__':
    num_squares(1)
