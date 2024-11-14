from typing import List


def generate_parenthesis(n: int) -> List[str]:
    ans = set()

    def backtrack(i, lst):
        if i == n:
            ans.add(''.join(lst))
            return

        # () ->0 ()()  () ->1 (())
        # ()()
        for j in range(0, len(lst) // 2 + 1):
            lst = lst[:j] + ['('] + [')'] + lst[j:]
            backtrack(i + 1, lst)
            lst = lst[:j] + lst[j + 2:]

    backtrack(0, [])
    return list(ans)


if __name__ == '__main__':
    print(generate_parenthesis(3))
