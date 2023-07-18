from collections import deque


def bfs(graph, start, visited):
    qu = deque([start])
    visited.append(start)
    while qu:
        v = qu.popleft()
        for node in graph[v]:
            if node not in visited:
                visited.append(node)
                qu.append(node)
    return visited


graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]
visited = []
print(bfs(graph, 1, visited))
