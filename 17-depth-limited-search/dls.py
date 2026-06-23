def dls(graph, start, goal, limit):
    print(f"Depth Limited Search (limit={limit})")
    print("=" * 40)

    def recursive_dls(node, goal, limit, path):
        print(f"Visiting: {node} | Depth: {len(path)-1}")
        if node == goal:
            print("=" * 40)
            print(f"Goal reached!")
            print(f"Path: {' -> '.join(path)}")
            return True
        if limit == 0:
            return False
        for neighbor in graph.get(node, []):
            if neighbor not in path:
                if recursive_dls(neighbor, goal, limit-1, path+[neighbor]):
                    return True
        return False

    result = recursive_dls(start, goal, limit, [start])
    if not result:
        print("Goal not found within depth limit.")

graph = {
    'A': ['B', 'D'],
    'B': ['E', 'C'],
    'D': ['E', 'H'],
    'E': ['F', 'H'],
    'H': ['G'],
    'F': ['C'],
    'C': [],
    'G': []
}

dls(graph, 'A', 'F', 3)