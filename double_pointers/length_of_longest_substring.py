def length_of_longest_substring(s: str) -> int:
    occ = set()
    left = 0
    max_len = 0
    for right in range(len(s)):
        while s[right] in occ:
            occ.remove(s[left])
            left += 1
        occ.add(s[right])
        max_len = max(max_len, right - left + 1)
    return max_len

