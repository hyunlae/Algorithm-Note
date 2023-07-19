from collections import deque


def bfs(graph, start, visited):
    qu = deque([start])
    visited[start] = True
    print(start, end=' ')
    while qu:
        v = qu.popleft()
        for i in graph[v]:
            if not visited[i]:
                print(i, end=' ')
                visited[i] = True
                qu.append(i)


def dfs(graph, start, visited):
    visited[start] = True

    print(start, end=' ')
    for i in graph[start]:
        if visited[i] == False:
            dfs(graph, i, visited)


n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]
dfs_visited = [False] * (n + 1)
bfs_visited = [False] * (n + 1)

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()

dfs(graph, v, dfs_visited)
print()
bfs(graph, v, bfs_visited)
