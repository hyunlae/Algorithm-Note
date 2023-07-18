from collections import deque


def bfs(graph, start):
    qu = deque([start])
    visited = [start]

    while qu:
        v = qu.popleft()
        for i in graph[v]:
            if i not in visited:
                qu.append(i)
                visited.append(i)

