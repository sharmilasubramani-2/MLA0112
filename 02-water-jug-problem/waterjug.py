from collections import deque

def water_jug_bfs(cap1, cap2, goal):
    visited = {(0, 0)}
    queue = deque([((0, 0), [(0, 0)])])

    while queue:
        (x, y), path = queue.popleft()
        if x == goal or y == goal:
            print("Goal reached! Path:")
            for state in path:
                print(state)
            return

        next_states = [
            (cap1, y), (x, cap2), (0, y), (x, 0),
            (x - min(x, cap2 - y), y + min(x, cap2 - y)),
            (x + min(y, cap1 - x), y - min(y, cap1 - x))
        ]
        for state in next_states:
            if state not in visited:
                visited.add(state)
                queue.append((state, path + [state]))

water_jug_bfs(4, 3, 2)