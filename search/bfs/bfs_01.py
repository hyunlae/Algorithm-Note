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
    print(visited)


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

bfs(graph, 1)
