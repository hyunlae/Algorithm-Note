def dfs(graph, start, visited):
    visited.append(start)

    for node in graph[start]:
        if node not in visited:
            dfs(graph, node, visited)


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
