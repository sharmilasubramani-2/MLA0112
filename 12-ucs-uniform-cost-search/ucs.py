def ucs(graph, start, goal):
    print("Uniform Cost Search")
    print("=" * 40)
    frontier = [[0, [start]]]
    visited = []
    while frontier:
        frontier.sort(key=lambda x: x[0])
        cost, path = frontier.pop(0)
        node = path[-1]
        if node in visited:
            continue
        visited.append(node)
        print(f"Visiting: {node} | Cost: {cost} | Path: {' -> '.join(path)}")
        if node == goal:
            print("=" * 40)
            print(f"Optimal Path : {' -> '.join(path)}")
            print(f"Total Cost   : {cost}")
            return
        for neighbor, edge_cost in graph.get(node, []):
            if neighbor not in visited:
                frontier.append([cost + edge_cost, path + [neighbor]])

graph = {
    'S': [('A', 1), ('G', 12)],
    'A': [('B', 3), ('C', 1)],
    'B': [('D', 3)],
    'C': [('D', 1), ('G', 2)],
    'D': [('G', 3)]
}
ucs(graph, 'S', 'G')