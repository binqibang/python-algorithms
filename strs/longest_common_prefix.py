def longest_common_prefix(strs: list[str]) -> str:
    prefix = strs[0]
    for i in range(1, len(strs)):
        prefix = str_prefix(prefix, strs[i])
    return prefix


def str_prefix(s: str, t: str):
    i = 0
    prefix = []
    while i < len(s) and i < len(t):
        if s[i] != t[i]:
            prefix.append(s[i])
        i += 1
    return "".join(prefix)
