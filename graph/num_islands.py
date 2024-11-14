from typing import List


def num_islands(grid: List[List[str]]) -> int:
    m, n = len(grid), len(grid[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def dfs(i: int, j: int):
        grid[i][j] = "0"
        for di, dj in directions:
            i1, j1 = i + di, j + dj
            if 0 <= i1 < m and 0 <= j1 < n and grid[i1][j1] == "1":
                dfs(i1, j1)

    cnt = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == "1":
                dfs(i, j)
                cnt += 1

    return cnt
