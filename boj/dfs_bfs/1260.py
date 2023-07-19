from collections import deque


def dfs(graph, start, visited=[]):

    visited.append(start)

    for i in graph[start]:
        if i not in visited:
            dfs(graph, i, visited)

    return visited


def bfs(graph, start, visited):

    qu = deque([start])
    visited.append(start)

    while qu:
        v = qu.popleft()
        for i in graph[v]:
            if i not in visited:
                visited.append(i)
                qu.append(i)

    return visited


n, m, v = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n + 1):
    graph[i].sort()

dfs_visited = []
bfs_visited = []
dfs_result = dfs(graph, v, dfs_visited)
bfs_result = bfs(graph, v, bfs_visited)
for i in dfs_result:
    print(i, end=' ')
print()
for i in bfs_result:
    print(i, end=' ')
