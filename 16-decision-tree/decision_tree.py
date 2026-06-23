import math

dataset = [
    ['Sunny','Hot','High','Weak','No'],
    ['Sunny','Hot','High','Strong','No'],
    ['Overcast','Hot','High','Weak','Yes'],
    ['Rain','Mild','High','Weak','Yes'],
    ['Rain','Cool','Normal','Weak','Yes'],
    ['Rain','Cool','Normal','Strong','No'],
    ['Overcast','Cool','Normal','Strong','Yes'],
    ['Sunny','Mild','High','Weak','No'],
    ['Sunny','Cool','Normal','Weak','Yes'],
    ['Rain','Mild','Normal','Weak','Yes'],
    ['Sunny','Mild','Normal','Strong','Yes'],
    ['Overcast','Mild','High','Strong','Yes'],
    ['Overcast','Hot','Normal','Weak','Yes'],
    ['Rain','Mild','High','Strong','No'],
]
attributes = ['Outlook','Temperature','Humidity','Wind']

def entropy(data):
    total = len(data)
    if total == 0: return 0
    counts = {}
    for row in data:
        counts[row[-1]] = counts.get(row[-1], 0) + 1
    return sum(-c/total * math.log2(c/total) for c in counts.values())

def info_gain(data, idx):
    total = len(data)
    values = set(row[idx] for row in data)
    weighted = sum(
        len([r for r in data if r[idx]==v])/total *
        entropy([r for r in data if r[idx]==v])
        for v in values)
    return entropy(data) - weighted

def build_tree(data, attr_indices, depth=0):
    indent = "  " * depth
    labels = [r[-1] for r in data]
    if len(set(labels)) == 1:
        print(f"{indent}-> Leaf: {labels[0]}")
        return
    if not attr_indices:
        print(f"{indent}-> Leaf (majority): {max(set(labels), key=labels.count)}")
        return
    gains = [(info_gain(data, i), i) for i in attr_indices]
    gains.sort(reverse=True)
    best_idx = gains[0][1]
    print(f"{indent}[{attributes[best_idx]}] (IG={gains[0][0]:.4f})")
    for v in sorted(set(row[best_idx] for row in data)):
        subset = [r for r in data if r[best_idx] == v]
        print(f"{indent}  {attributes[best_idx]} = {v}:")
        build_tree(subset, [i for i in attr_indices if i != best_idx], depth+2)

print("Decision Tree - Play Tennis")
print("=" * 40)
print(f"Overall Entropy: {entropy(dataset):.4f}")
print("=" * 40)
build_tree(dataset, list(range(4)))