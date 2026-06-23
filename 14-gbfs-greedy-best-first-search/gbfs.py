def gbfs(graph, heuristic, start, goal):
    print("Greedy Best First Search (GBFS)")
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
            print(f"Path : {' -> '.join(path)}")
            return
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                frontier.append([heuristic[neighbor], path + [neighbor]])

graph = {
    'P': ['R', 'G', 'A'],
    'R': ['E'],
    'G': ['C', 'U'],
    'A': ['M'],
    'C': ['U'],
    'U': ['M', 'S'],
    'M': ['N', 'L'],
    'L': ['N'],
    'N': ['S'],
    'E': ['S'],
    'S': []
}
heuristic = {
    'P': 10, 'R': 8, 'G': 6, 'A': 11,
    'C': 4,  'U': 4, 'M': 9, 'L': 9,
    'E': 3,  'N': 6, 'S': 0
}
gbfs(graph, heuristic, 'P', 'S')