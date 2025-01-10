from typing import List


def oranges_rotting(grid: List[List[int]]) -> int:
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    rotting_queue = []
    m, n = len(grid), len(grid[0])
    fresh_orange = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 2:
                rotting_queue.append((i, j))
            elif grid[i][j] == 1:
                fresh_orange += 1

    step = 0
    while fresh_orange > 0 and len(rotting_queue) > 0:
        step += 1
        curr_queue_size = len(rotting_queue)
        for i in range(curr_queue_size):
            curr_orange = rotting_queue[0]
            rotting_queue.pop(0)
            for dx, dy in dirs:
                x = curr_orange[0] + dx
                y = curr_orange[1] + dy
                if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                    grid[x][y] = 2
                    rotting_queue.append((x, y))
                    fresh_orange -= 1

    if fresh_orange == 0:
        return step
    else:
        return -1


if __name__ == '__main__':
    grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    oranges_rotting(grid)
