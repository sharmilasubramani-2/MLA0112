def hill_climbing():
    print("Hill Climbing - Blocks World")
    print("=" * 40)
    start = ['D', 'C', 'B', 'A']
    goal  = ['A', 'B', 'C', 'D']

    def score(state):
        return sum(1 for i in range(len(state)) if state[i] == goal[i])

    current = start[:]
    print(f"Start : {current} | Score: {score(current)}")
    print(f"Goal  : {goal}")
    print("-" * 40)
    step = 1
    while current != goal:
        best = None
        best_score = score(current)
        for i in range(len(current)):
            for j in range(len(current)):
                if i != j:
                    new = current[:]
                    new[i], new[j] = new[j], new[i]
                    if score(new) > best_score:
                        best_score = score(new)
                        best = new[:]
        if best is None:
            print("Stuck at local maximum.")
            break
        current = best
        print(f"Step {step}: {current} | Score: {score(current)}")
        step += 1
    if current == goal:
        print("=" * 40)
        print(f"Goal reached in {step-1} steps!")
        print(f"Final State: {current}")

hill_climbing()