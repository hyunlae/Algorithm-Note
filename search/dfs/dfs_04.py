def dfs(graph, start, visited=[]):
    visited.append(start)

    for i in graph[start]:
        if i not in visited:
            dfs(graph, i, visited)

    return visited


graph = {'A': ['B', 'C'],
         'B': ['A', 'D', 'E'],
         'C': ['A', 'G', 'H'],
         'D': ['B'],
         'E': ['B', 'F'],
         'F': ['E'],
         'G': ['C'],
         'H': ['C']}

visited = []
dfs(graph, 'A', visited)
print(visited)
