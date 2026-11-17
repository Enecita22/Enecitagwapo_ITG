
from collections import deque

# Create graph
graph = {
    'E': ['N', 'T'],
    'C': ['N', 'T'],
    'I': ['N', 'T'],
    'N': ['E', 'C', 'I'],
    'T': ['E', 'C', 'I']
}

# Breadth-First Search
def BFS(start):
    visited = []
    queue = deque([start])

    visited.append(start)

    while queue:
        current = queue.popleft()
        print(current, end=" ")

        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)

# Depth-First Search
def DFS(current, visited):
    visited.append(current)
    print(current, end=" ")

    for neighbor in graph[current]:
        if neighbor not in visited:
            DFS(neighbor, visited)


# Main Program
print("GRAPH - ENECITA")
print("----------------")

print("BFS: ", end="")
BFS('E')

print("\nDFS: ", end="")
DFS('E', [])

print()
