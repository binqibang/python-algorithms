from typing import List


def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    edges = [[] for _ in range(numCourses)]
    indegree = [0] * numCourses
    for u, v in prerequisites:
        edges[v].append(u)
        indegree[u] += 1
    queue = [u for u in range(numCourses) if indegree[u] == 0]
    visited = 0
    while len(queue) > 0:
        visited += 1
        u = queue[0]
        queue.pop(0)
        for v in edges[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                queue.append(v)

    return visited == numCourses
