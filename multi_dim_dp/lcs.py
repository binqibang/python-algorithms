def longest_common_subsequence(text1: str, text2: str) -> int:
    """
    求最长公共子序列的长度
    :param text1: 第一个字符串
    :param text2: 第二个字符串
    :return: 最长公共子序列的长度
    """
    max_len = 0
    m, n = len(text1), len(text2)
    # lcs of text1[:i] and text2[:j]
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # 当前字符相同时，当前长度的最长公共子序列长度加1
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                # 当前字符不同时，取两个子问题的最大值
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
            max_len = max(dp[i][j], max_len)

    return max_len


if __name__ == '__main__':
    text1 = "bsbininm"
    text2 = "jmjkbkjkv"
    longest_common_subsequence(text1, text2)
