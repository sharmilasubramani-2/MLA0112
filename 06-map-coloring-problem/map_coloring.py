def is_valid(state, graph, node, color):
    for neighbor in graph[node]:
        if state.get(neighbor) == color:
            return False
    return True

def backtrack(state, colors, graph, nodes):
    if len(state) == len(nodes):
        return state
    node = [n for n in nodes if n not in state][0]
    for color in colors:
        if is_valid(state, graph, node, color):
            state[node] = color
            result = backtrack(state, colors, graph, nodes)
            if result:
                return result
            del state[node]
    return None

graph = {
    'Chennai': ['Thiruvanmiyur', 'Vellore'],
    'Thiruvanmiyur': ['Chennai', 'Vellore'],
    'Vellore': ['Chennai', 'Thiruvanmiyur', 'Hyderabad'],
    'Hyderabad': ['Vellore']
}
nodes = list(graph.keys())
colors = ['Red', 'Green', 'Blue']

solution = backtrack({}, colors, graph, nodes)
print("Map Coloring Solution:")
for state, color in solution.items():
    print(f"{state} -> {color}")