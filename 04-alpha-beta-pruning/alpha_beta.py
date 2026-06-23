import math

def alphabeta(depth, node_index, is_max, scores, alpha, beta, h):
    if depth == h:
        return scores[node_index]
    if is_max:
        best = -math.inf
        for i in range(2):
            val = alphabeta(depth+1, node_index*2+i, False, scores, alpha, beta, h)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best
    else:
        best = math.inf
        for i in range(2):
            val = alphabeta(depth+1, node_index*2+i, True, scores, alpha, beta, h)
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best

scores = [3, 5, 2, 9, 12, 5, 23, 23]
h = int(math.log2(len(scores)))
print("Optimal value (Alpha-Beta):", alphabeta(0, 0, True, scores, -math.inf, math.inf, h))