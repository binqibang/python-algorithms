from typing import List


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    ans = []
    anagram_map = dict()
    for word in strs:
        count = [0] * 26
        for ch in word:
            count[ord(ch) - ord('a')] += 1
        k = str(count)
        if k in anagram_map:
            anagram_map[k].append(word)
        else:
            anagram_map[k] = [word]
    for k, v in anagram_map.items():
        ans.append(v)
    return ans


if __name__ == '__main__':
    print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    print([])
    print(['a'])
