# Experiment 01 - Breadth First Search (BFS)

## Aim
To implement Breadth First Search (BFS) using Python.

## Algorithm

1. Create the graph.
2. Create an empty queue.
3. Insert the starting node.
4. Remove the front node.
5. Visit all adjacent unvisited nodes.
6. Repeat until the queue becomes empty.

## Pseudocode

```text
BFS(Graph, Start)

Create Queue
Create Visited Set

Enqueue(Start)

While Queue is not empty

    Node = Dequeue()

    Print Node

    For every adjacent node

        If node is not visited

            Mark visited

            Enqueue(node)
```

## Python Program

Refer to **bfs.py**

## Output

```
BFS Traversal:
A B C D E F G
```

## Result

Breadth First Search was implemented successfully.