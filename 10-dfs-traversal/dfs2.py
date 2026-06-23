def dfs(graph, start, visited=None):
    if visited is None:
        visited = []
        print("DFS - Lettered Graph")
        print("=" * 40)
    visited.append(start)
    print(f"Visited: {start}")
    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    if len(visited) == len(graph):
        print("=" * 40)
        print(f"DFS Order: {' -> '.join(visited)}")
    return visited

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': ['G'],
    'G': []
}
dfs(graph, 'A')