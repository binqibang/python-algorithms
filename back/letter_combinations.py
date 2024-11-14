from typing import List


def letter_combinations(digits: str) -> List[str]:
    letter_map = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }

    combs = []
    stack = []
    n = len(digits)

    def backtrack(i):
        if len(stack) == n:
            combs.append(''.join(stack))
            return
        letters = letter_map[digits[i]]
        for j in range(0, len(letters)):
            stack.append(letters[j])
            backtrack(i + 1)
            stack.pop()

    backtrack(0)
    return combs


if __name__ == '__main__':
    print(letter_combinations('5959'))
