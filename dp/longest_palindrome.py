def longestPalindrome(s: str) -> str:
    """
    给定一个字符串 s，找到 s 中最长的回文子串
    :param s: 输入字符串
    :return: 最长的回文子串
    """
    n = len(s)
    if n <= 1:
        return s
    max_len, max_start = 0, 0

    for i in range(n):
        curr_len = 1
        left, right = i - 1, i + 1
        # 左右边界扩散，是否是相同字符
        while left >= 0 and s[left] == s[i]:
            left -= 1
            curr_len += 1
        while right < n and s[right] == s[i]:
            right += 1
            curr_len += 1
        # 中心扩散
        while left >= 0 and right < n and s[left] == s[right]:
            left -= 1
            right += 1
            curr_len += 2
        if curr_len > max_len:
            max_len = curr_len
            max_start = left + 1
    # print(max_start, max_len, max_start + max_len)
    return s[max_start: max_start + max_len]


if __name__ == '__main__':
    print(longestPalindrome("aa"))
