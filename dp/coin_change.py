from typing import List


def coin_change(coins: List[int], amount: int) -> int:
    n = len(coins)
    # 初始化 dp 数组，dp[i][j] 表示使用前 i 种硬币凑成金额 j 所需的最少硬币个数
    dp = [[float('inf')] * (amount + 1) for _ in range(n + 1)]

    # 凑成金额 0 所需的硬币个数为 0
    for i in range(n + 1):
        dp[i][0] = 0

    # 填充 dp 数组
    for i in range(1, n + 1):
        for j in range(1, amount + 1):
            # 不使用第 i 种硬币
            dp[i][j] = dp[i - 1][j]
            # 使用第 i 种硬币
            if j >= coins[i - 1]:
                dp[i][j] = min(dp[i][j], dp[i][j - coins[i - 1]] + 1)

    # 返回结果
    return dp[n][amount] if dp[n][amount] != float('inf') else -1


def coin_change_ii(coins: List[int], amount: int) -> int:
    n = len(coins)
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    # for i in range(1, n + 1):
    #     for j in range(coins[i - 1], amount + 1):
    #         dp[j] = min(dp[j], dp[j - coins[i - 1]] + 1)
    for i in range(n):
        for j in range(coins[i], amount + 1):
            dp[j] = min(dp[j], dp[j - coins[i]])

    return dp[amount] if dp[amount] != float('inf') else -1


if __name__ == '__main__':
    coins = [1, 2, 5]
    amount = 5
    coin_change(coins, amount)
