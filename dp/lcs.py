def longestCommonSubsequence(text1: str, text2: str) -> int:
    # abcde ace
    max_len = 0
    m, n = len(text1), len(text2)
    # lcs of text1[:i] and text2[:j]
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
            max_len = max(dp[i][j], max_len)

    return max_len


if __name__ == '__main__':
    text1 = "bsbininm"
    text2 = "jmjkbkjkv"
    longestCommonSubsequence(text1, text2)
