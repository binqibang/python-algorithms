from typing import List


def find_order(numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    edges = [[] for _ in range(numCourses)]
    indegree = [0] * numCourses
    for u, v in prerequisites:
        edges[v].append(u)
        indegree[u] += 1
    order = []
    queue = [u for u in range(numCourses) if indegree[u] == 0]
    while queue:
        u = queue[0]
        queue.pop(0)
        order.append(u)
        for v in edges[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                queue.append(v)
    if len(order) == numCourses:
        return order
    else:
        return []
