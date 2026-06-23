from collections import deque

def is_valid(state):
    ml, cl, boat, mr, cr = state
    if ml < 0 or cl < 0 or mr < 0 or cr < 0:
        return False
    if ml > 0 and ml < cl:
        return False
    if mr > 0 and mr < cr:
        return False
    return True

def get_next_states(state):
    ml, cl, boat, mr, cr = state
    moves = [(1,0), (2,0), (0,1), (0,2), (1,1)]
    next_states = []
    for m, c in moves:
        if boat == 1:
            new_state = (ml-m, cl-c, 0, mr+m, cr+c)
        else:
            new_state = (ml+m, cl+c, 1, mr-m, cr-c)
        if is_valid(new_state):
            next_states.append(new_state)
    return next_states

def bfs():
    start = (3, 3, 1, 0, 0)
    goal = (0, 0, 0, 3, 3)
    visited = {start}
    queue = deque([(start, [start])])
    while queue:
        state, path = queue.popleft()
        if state == goal:
            print("Solution Path:")
            for s in path:
                print(s)
            return
        for next_state in get_next_states(state):
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, path + [next_state]))

bfs()