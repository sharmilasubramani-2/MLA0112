def a_star(graph, heuristic, start, goal):
    print("A* Search")
    print("=" * 40)
    frontier = [[heuristic[start], 0, [start]]]
    visited = []
    while frontier:
        frontier.sort(key=lambda x: x[0])
        f, g, path = frontier.pop(0)
        node = path[-1]
        if node in visited:
            continue
        visited.append(node)
        print(f"Visiting: {node} | g={g}, h={heuristic[node]}, f={f} | Path: {' -> '.join(path)}")
        if node == goal:
            print("=" * 40)
            print(f"Optimal Path : {' -> '.join(path)}")
            print(f"Total Cost   : {g}")
            return
        for neighbor, cost in graph.get(node, []):
            if neighbor not in visited:
                new_g = g + cost
                frontier.append([new_g + heuristic[neighbor], new_g, path + [neighbor]])

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 3), ('E', 2)],
    'C': [('E', 5)],
    'D': [('G', 2), ('F', 1)],
    'E': [('G', 3)],
    'F': [('G', 1)],
    'G': []
}
heuristic = {'A': 5, 'B': 6, 'C': 4, 'D': 3, 'E': 3, 'F': 1, 'G': 0}
a_star(graph, heuristic, 'A', 'G')