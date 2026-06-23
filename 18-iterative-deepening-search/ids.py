def ids(graph, start, goal, max_depth):
    print("Iterative Deepening Search (IDS)")
    print("=" * 40)

    def dls(node, goal, limit, path):
        if node == goal:
            return path
        if limit == 0:
            return None
        for neighbor in graph.get(node, []):
            if neighbor not in path:
                result = dls(neighbor, goal, limit-1, path+[neighbor])
                if result:
                    return result
        return None

    for depth in range(max_depth + 1):
        print(f"Iteration I{depth} | Depth limit = {depth}")
        result = dls(start, goal, depth, [start])
        if result:
            print("=" * 40)
            print(f"Goal reached!")
            print(f"Path: {' -> '.join(result)}")
            return result
        print(f"Goal not found at depth {depth}")

    print("Goal not found.")
    return None

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E', 'F'],
    'C': ['G'],
    'D': ['H', 'I'],
    'E': ['F'],
    'F': ['G'],
    'G': ['J'],
    'H': [],
    'I': [],
    'J': []
}

ids(graph, 'A', 'J', 4)