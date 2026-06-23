def gbfs(graph, heuristic, start, goal):
    print("Greedy Best First Search (GBFS) - Graph 2")
    print("=" * 40)
    frontier = [[heuristic[start], [start]]]
    visited = []
    while frontier:
        frontier.sort(key=lambda x: x[0])
        h_val, path = frontier.pop(0)
        node = path[-1]
        if node in visited:
            continue
        visited.append(node)
        print(f"Visiting: {node} | h={h_val} | Path: {' -> '.join(path)}")
        if node == goal:
            print("=" * 40)
            print(f"Goal reached!")
            print(f"Path : {' -> '.join(path)}")
            return
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                frontier.append([heuristic[neighbor], path + [neighbor]])

graph = {
    'A': ['B', 'D', 'C'],
    'B': ['E'],
    'D': ['F'],
    'C': ['E', 'F'],
    'E': ['H'],
    'F': ['G'],
    'H': ['G'],
    'G': []
}
heuristic = {
    'A': 40, 'B': 32, 'D': 35,
    'C': 25, 'E': 19, 'F': 17,
    'H': 10, 'G': 0
}
gbfs(graph, heuristic, 'A', 'G')