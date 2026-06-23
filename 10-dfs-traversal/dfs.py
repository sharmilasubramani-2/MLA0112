graph = {
    1: [2, 3], 2: [1, 4, 5], 3: [1, 6],
    4: [2], 5: [2, 6], 6: [3, 5, 7],
    7: [6, 8], 8: [7, 9], 9: [8]
}

def dfs(start, visited=None):
    if visited is None:
        visited = []
    visited.append(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(neighbor, visited)
    return visited

print("DFS Traversal:", dfs(1))