def dfs(graph, start):
    stack = [start]
    visited = []

    while stack:
        v = stack.pop()
        if v not in visited:
            visited.append(v)
            stack.extend(graph[v])
    print(visited)


graph = {'A': ['B', 'C'],
         'B': ['A', 'D', 'E'],
         'C': ['A', 'G', 'H'],
         'D': ['B'],
         'E': ['B', 'F'],
         'F': ['E'],
         'G': ['C'],
         'H': ['C']}
dfs(graph, 'A')
