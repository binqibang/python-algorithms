from typing import List


def exist(board: List[List[str]], word: str) -> bool:
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    m, n = len(board), len(board[0])

    def dfs(i: int, j: int, k: int) -> bool:
        if k == len(word) - 1:
            return word[-1] == board[i][j]
        if board[i][j] != word[k]:
            return False
        tmp = board[i][j]
        board[i][j] = '*'
        for di, dj in directions:
            i1, j1 = i + di, j + dj
            if 0 <= i1 < m and 0 <= j1 < n and board[i1][j1] != '*':
                if dfs(i1, j1, k + 1):
                    return True
                break
        board[i][j] = tmp
        return False

    for i in range(m):
        for j in range(n):
            if dfs(i, j, 0):
                return True

    return False
