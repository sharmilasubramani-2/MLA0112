# AI Expert System Lab - MLA0112

## Programs List

---

### 01 - N Queens Problem
**Pseudocode:**
BEGIN N_QUEENS(n):

Place queens one by one in each row

FOR each column in current row:

IF queen is safe (no attack):

Place queen

RECURSIVELY solve next row

IF solution found: RETURN True

Remove queen (backtrack)

RETURN False

END

---

### 02 - Water Jug Problem
**Pseudocode:**
BEGIN WATER_JUG(start, goal):

stack = [start]

visited = []

WHILE stack not empty:

state = stack.pop()

IF state == goal: RETURN path

FOR each possible action (fill, empty, pour):

new_state = apply action

IF not visited: ADD to stack

END

---

### 03 - Minimax Algorithm
**Pseudocode:**
BEGIN MINIMAX(node, depth, isMaximizing):

IF depth == 0 or terminal: RETURN score

IF isMaximizing:

best = -infinity

FOR each child:

best = MAX(best, MINIMAX(child, depth-1, False))

ELSE:

best = +infinity

FOR each child:

best = MIN(best, MINIMAX(child, depth-1, True))

RETURN best

END

---

### 04 - Alpha Beta Pruning
**Pseudocode:**
BEGIN ALPHA_BETA(node, depth, alpha, beta, isMaximizing):

IF depth == 0 or terminal: RETURN score

IF isMaximizing:

FOR each child:

alpha = MAX(alpha, ALPHA_BETA(child, depth-1, alpha, beta, False))

IF alpha >= beta: BREAK (prune)

RETURN alpha

ELSE:

FOR each child:

beta = MIN(beta, ALPHA_BETA(child, depth-1, alpha, beta, True))

IF beta <= alpha: BREAK (prune)

RETURN beta

END

---

### 05 - Cryptarithmetic Problem
**Pseudocode (SEND+MORE=MONEY):**
BEGIN CRYPTARITHMETIC():

FOR each permutation of digits 0-9:

Assign digits to letters

IF leading digits != 0:

IF equation holds: PRINT solution

END
**Pseudocode (TWO+TWO=FOUR):**
BEGIN TWO_PLUS_TWO():

FOR each permutation of 6 digits from 0-9:

Assign T, W, O, F, U, R

IF T != 0 AND F != 0:

TWO = T100 + W10 + O

FOUR = F1000 + O100 + U*10 + R

IF TWO + TWO == FOUR: PRINT solution

END

---

### 06 - Map Coloring Problem
**Pseudocode:**
BEGIN MAP_COLORING(graph, colors):

FOR each region:

FOR each color:

IF no adjacent region has same color:

Assign color

RECURSIVELY color next region

IF solution found: RETURN True

Remove color (backtrack)

RETURN False

END

---

### 07 - Missionaries and Cannibals
**Pseudocode:**
BEGIN MISSIONARIES_CANNIBALS(start, goal):

queue = [start]

visited = []

WHILE queue not empty:

state = queue.pop(0)

IF state == goal: RETURN path

FOR each valid move:

new_state = apply move

IF safe and not visited: ADD to queue

END

---

### 08 - Tic Tac Toe Minimax
**Pseudocode:**
BEGIN TIC_TAC_TOE():

WHILE game not over:

IF human turn: GET human move

IF AI turn:

best_move = MINIMAX(board, True)

Apply best_move

CHECK winner

END

---

### 09 - BFS Traversal
**Pseudocode:**
BEGIN BFS(graph, start):

queue = [start]

visited = []

WHILE queue not empty:

node = queue.pop(0)

IF not visited:

ADD to visited; PRINT

FOR each neighbor:

IF not visited: ADD to queue

END

---

### 10 - DFS Traversal
**Pseudocode:**
BEGIN DFS(graph, start):

ADD start to visited; PRINT

FOR each neighbor of start:

IF not visited:

RECURSIVELY call DFS(neighbor)

END

---

### 11 - Jug Riddle Problem
**Pseudocode:**
BEGIN JUG_RIDDLE(start, goal):

stack = [start]

visited = []

WHILE stack not empty:

state = stack.pop()

IF state == goal: RETURN path

FOR each valid move:

new_state = apply move

IF not visited: ADD to stack

END

---

### 12 - Uniform Cost Search (UCS)
**Pseudocode:**
BEGIN UCS(graph, start, goal):

frontier = [[0, [start]]]

visited = []

WHILE frontier not empty:

Sort frontier by cost

cost, path = frontier.pop(0)

node = last in path

IF node in visited: CONTINUE

ADD to visited

IF node == goal: PRINT path, cost; RETURN

FOR each neighbor, edge_cost:

ADD [cost+edge_cost, path+neighbor] to frontier

END

---

### 13 - A* Search
**Pseudocode:**
BEGIN A_STAR(graph, heuristic, start, goal):

frontier = [[h[start], 0, [start]]]

visited = []

WHILE frontier not empty:

Sort by f value

f, g, path = frontier.pop(0)

node = last in path

IF node in visited: CONTINUE

ADD to visited

IF node == goal: PRINT path, cost; RETURN

FOR each neighbor, cost:

new_g = g + cost

new_f = new_g + h[neighbor]

ADD [new_f, new_g, path+neighbor] to frontier

END

---

### 14 - Greedy Best First Search (GBFS)
**Pseudocode:**
BEGIN GBFS(graph, heuristic, start, goal):

frontier = [[h[start], [start]]]

visited = []

WHILE frontier not empty:

Sort by h value

h_val, path = frontier.pop(0)

node = last in path

IF node in visited: CONTINUE

ADD to visited

IF node == goal: PRINT path; RETURN

FOR each neighbor:

IF not visited: ADD [h[neighbor], path+neighbor]

END

---

### 15 - Hill Climbing
**Pseudocode:**
BEGIN HILL_CLIMBING():

current = start_state

WHILE current != goal:

best = None

best_score = score(current)

FOR each possible swap:

new_state = apply swap

IF score(new_state) > best_score:

best = new_state

IF best is None: PRINT "Local max"; BREAK

current = best; PRINT state

IF current == goal: PRINT "Goal reached"

END

---

### 16 - Decision Tree
**Pseudocode:**
BEGIN DECISION_TREE(data, attributes):

IF all labels same: RETURN leaf node

IF no attributes: RETURN majority label

best_attr = attribute with highest Information Gain

PRINT best_attr

FOR each value of best_attr:

subset = rows where best_attr == value

RECURSIVELY build_tree(subset, remaining_attributes)

END
17 - Depth Limited Search
BEGIN DLS(graph, start, goal, limit):
  CALL recursive_dls(start, goal, limit, [start])

BEGIN recursive_dls(node, goal, limit, path):
  PRINT node
  IF node == goal: PRINT path; RETURN True
  IF limit == 0: RETURN False
  FOR each neighbor of node:
    IF neighbor not in path:
      CALL recursive_dls(neighbor, goal, limit-1, path+neighbor)
      IF result True: RETURN True
  RETURN False
END

18 - Iterative Deepening Search
BEGIN IDS(graph, start, goal, max_depth):
  FOR depth = 0 to max_depth:
    PRINT "Iteration depth"
    result = DLS(start, goal, depth, [start])
    IF result found: PRINT path; RETURN
    PRINT "Not found at this depth"
  PRINT "Goal not found"
END

BEGIN DLS(node, goal, limit, path):
  IF node == goal: RETURN path
  IF limit == 0: RETURN None
  FOR each neighbor of node:
    IF neighbor not in path:
      result = DLS(neighbor, goal, limit-1, path+neighbor)
      IF result: RETURN result
  RETURN None
END

19 - Neural Network
BEGIN NEURAL_NETWORK():
  Initialize weights w1, w2 and biases b1, b2 randomly

  FORWARD PASS:
    FOR each hidden neuron:
      total = bias + SUM(input * weight)
      hidden = sigmoid(total)
    total = bias + SUM(hidden * weight)
    output = sigmoid(total)

  BACKPROPAGATION:
    output_error = target - output
    output_delta = output_error * sigmoid_derivative(output)
    FOR each hidden neuron:
      hidden_error = output_delta * weight
      hidden_delta = hidden_error * sigmoid_derivative(hidden)
    UPDATE output weights += learning_rate * output_delta * hidden
    UPDATE hidden weights += learning_rate * hidden_delta * input

  TRAINING:
    FOR 10000 epochs:
      FOR each input in dataset:
        CALL forward pass
        CALL backpropagation

  TESTING:
    FOR each input: PRINT predicted output
END
### 17 - Depth Limited Search
**Pseudocode:**
BEGIN DLS(graph, start, goal, limit):

CALL recursive_dls(start, goal, limit, [start])
BEGIN recursive_dls(node, goal, limit, path):

PRINT node

IF node == goal: PRINT path; RETURN True

IF limit == 0: RETURN False

FOR each neighbor of node:

IF neighbor not in path:

CALL recursive_dls(neighbor, goal, limit-1, path+neighbor)

IF result True: RETURN True

RETURN False

END

---

### 18 - Iterative Deepening Search
**Pseudocode:**
BEGIN IDS(graph, start, goal, max_depth):

FOR depth = 0 to max_depth:

PRINT "Iteration depth"

result = DLS(start, goal, depth, [start])

IF result found: PRINT path; RETURN

PRINT "Not found at this depth"

PRINT "Goal not found"

END
BEGIN DLS(node, goal, limit, path):

IF node == goal: RETURN path

IF limit == 0: RETURN None

FOR each neighbor of node:

IF neighbor not in path:

result = DLS(neighbor, goal, limit-1, path+neighbor)

IF result: RETURN result

RETURN None

END

---

### 19 - Neural Network
**Pseudocode:**
BEGIN NEURAL_NETWORK():

Initialize weights w1, w2 and biases b1, b2
FORWARD PASS:

FOR each hidden neuron:

total = bias + SUM(input * weight)

hidden = sigmoid(total)

output = sigmoid(bias + SUM(hidden * weight))
BACKPROPAGATION:

output_error = target - output

output_delta = output_error * sigmoid_derivative(output)

FOR each hidden neuron:

hidden_delta = output_delta * weight * sigmoid_derivative(hidden)

UPDATE weights and biases using learning_rate
TRAINING:

FOR 10000 epochs:

FOR each input: forward pass + backpropagation
TESTING:

FOR each input: PRINT predicted output

END