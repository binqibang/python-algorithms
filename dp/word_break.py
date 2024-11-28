from typing import List


def word_break(s: str, word_dict: List[str]) -> bool:
    word_set = set(word_dict)
    n = len(s)
    # dp[i] 表示 s[0:i] 是否可以由 word_dict 拼接而成
    dp = [False] * (n + 1)
    dp[0] = True
    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j: i] in word_set:
                dp[i] = True
                break
    return dp[n]
