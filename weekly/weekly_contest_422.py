from typing import List
import heapq


class WeeklyContest422:
    def isBalanced(self, num: str) -> bool:
        odd_sum, even_sum = 0, 0
        for i, ch in enumerate(num):
            if i % 2 == 0:
                even_sum += int(ch)
            else:
                odd_sum += int(ch)

        return odd_sum == even_sum

    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        m, n = len(moveTime), len(moveTime[0])
        distance = [[float('inf')] * n for _ in range(m)]
        # print(distance)
        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1),
        ]
        distance[0][0] = 0
        queue = [(0, 0, 0)]
        while queue:
            i, j, time = queue[0]
            queue.pop(0)
            for dx, dy in directions:
                x, y = i + dx, j + dy
                if 0 <= x < m and 0 <= y < n:
                    if moveTime[x][y] <= time:
                        new_time = time + 1
                        if new_time < distance[x][y]:
                            distance[x][y] = new_time
                            queue.append((x, y, new_time))
                    else:
                        new_time = moveTime[x][y] + 1
                        distance[x][y] = new_time
                        queue.append((x, y, new_time))
        return distance[m - 1][n - 1]

    def minTimeToReachII(self, moveTime: List[List[int]]) -> int:
        m, n = len(moveTime), len(moveTime[0])
        dp = [[float('inf')] * n for _ in range(m)]
        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1),
        ]
        dp[0][0] = 0
        prior_queue = [(0, 0, 0, 0)]
        while len(prior_queue) > 0:
            time, i, j, step = heapq.heappop(prior_queue)
            for dx, dy in directions:
                x, y = i + dx, j + dy
                if 0 <= x < m and 0 <= y < n:
                    if moveTime[x][y] < time:
                        new_time = time + step % 2 + 1
                        if new_time < dp[x][y]:
                            dp[x][y] = new_time
                            heapq.heappush(prior_queue, (new_time, x, y, step + 1))
                    else:
                        new_time = moveTime[x][y] + step % 2 + 1
                        if new_time < dp[x][y]:
                            dp[x][y] = new_time
                            heapq.heappush(prior_queue, (new_time, x, y, step + 1))

        return dp[m - 1][n - 1]


if __name__ == '__main__':
    wc = WeeklyContest422()
    print(wc.minTimeToReach([[3, 72, 14], [25, 81, 5]]))
