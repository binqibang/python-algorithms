from typing import List


def partition(s: str) -> List[List[str]]:
    """
    对字符串s进行分割，使得每个分割出的子字符串都是回文串。
    :param s: 需要分割的字符串
    :return:一个列表，包含所有可能的分割方案，每个方案都是一个包含回文子字符串的列表。
    """
    n = len(s)
    # 初始化动态规划表格，用于记录子字符串是否为回文串
    dp = [[False] * n for _ in range(n)]

    # 单个字符是回文串
    for i in range(n):
        dp[i][i] = True

    # 两个连续字符是回文串
    for i in range(n - 1):
        dp[i][i + 1] = s[i] == s[i + 1]

    # 填充动态规划表格，判断所有子字符串是否为回文串
    for i in range(n - 3, -1, -1):
        for j in range(i + 2, n):
            dp[i][j] = dp[i + 1][j - 1] & (s[i] == s[j])

    # 初始化结果列表和当前分割方案列表
    ans = []
    substr_lst = []

    def backtrack(i):
        # 如果起始位置到达字符串末尾，将当前分割方案加入结果列表
        if i == n:
            ans.append(substr_lst[:])
            return
        # 尝试所有可能的分割位置
        for j in range(i, n):
            # 如果当前子字符串是回文串，添加到当前分割方案，并继续回溯
            if dp[i][j]:
                substr_lst.append(s[i: j + 1])
                backtrack(j + 1)
                # 回溯，移除最后一个添加的子字符串
                substr_lst.pop()

    # 从字符串起始位置开始回溯
    backtrack(0)
    return ans


if __name__ == '__main__':
    print(partition('abb'))
