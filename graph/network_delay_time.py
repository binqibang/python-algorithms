from typing import List


def networkDelayTime(times: List[List[int]], n: int, k: int) -> int:
    INF = float('inf') / 2
    adj_mat = [[INF] * n for _ in range(n)]


