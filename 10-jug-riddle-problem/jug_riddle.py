from collections import deque

def jug_riddle_bfs(capacities, start, goal):
    visited = {start}
    queue = deque([(start, [start])])
    while queue:
        state, path = queue.popleft()
        if state[0] == goal[0] and state[1] == goal[1]:
            print("Solution Path:")
            for s in path:
                print(s)
            return
        for i in range(3):
            for j in range(3):
                if i == j:
                    continue
                new_state = list(state)
                amount = min(state[i], capacities[j] - state[j])
                new_state[i] -= amount
                new_state[j] += amount
                new_state = tuple(new_state)
                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((new_state, path + [new_state]))

capacities = (12, 8, 5)
jug_riddle_bfs(capacities, (12, 0, 0), (6, 6, 0))