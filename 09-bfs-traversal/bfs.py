from collections import deque

graph = {
    1: [2, 3], 2: [1, 4, 5], 3: [1, 6],
    4: [2], 5: [2, 6], 6: [3, 5, 7],
    7: [6, 8], 8: [7, 9], 9: [8]
}

def bfs(start):
    visited = [start]
    queue = deque([start])
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)
    return visited

print("BFS Traversal:", bfs(1))