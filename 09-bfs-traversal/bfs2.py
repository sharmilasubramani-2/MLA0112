def bfs(graph, start):
    print("BFS - Lettered Graph")
    print("=" * 40)
    visited = []
    queue = [start]
    while queue:
        node = queue.pop(0)
        if node in visited:
            continue
        visited.append(node)
        print(f"Visited: {node}")
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                queue.append(neighbor)
    print("=" * 40)
    print(f"BFS Order: {' -> '.join(visited)}")

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': ['F'],
    'F': ['G'],
    'G': []
}
bfs(graph, 'A')