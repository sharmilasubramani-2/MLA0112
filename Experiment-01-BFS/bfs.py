from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['C', 'D', 'E'],
    'C': ['F', 'G'],
    'D': ['E'],
    'E': ['F'],
    'F': ['G'],
    'G': []
}

visited = set()
queue = deque(['A'])

print("BFS Traversal:")

while queue:
    node = queue.popleft()

    if node not in visited:
        print(node, end=" ")
        visited.add(node)

        for neighbour in graph[node]:
            if neighbour not in visited:
                queue.append(neighbour)