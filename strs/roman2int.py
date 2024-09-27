
def roman2int(s: str) -> int:
    trans = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    ans = 0
    n = len(s)
    for i, ch in enumerate(s):
        v = trans[ch]
        # 右边数字比左边数字大，减去该数
        if i < n - 1 and v < trans[s[i + 1]]:
            ans -= v
        else:
            ans += v
    return ans

