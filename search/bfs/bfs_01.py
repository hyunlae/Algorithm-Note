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


graph = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': [],
    '4': ['8'],
    '8': []
}

bfs(graph, '5')
