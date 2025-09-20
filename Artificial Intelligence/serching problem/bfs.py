from collections import deque  # Import deque for efficient queue operations

# Define the tree as a dictionary (adjacency list)
tree = {
    'A': ['B', 'E'],
    'B': ['C', 'D'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

def bfs(tree, start):
    visited = set()              # Set to keep track of visited nodes
    queue = deque([start])       # Initialize queue with the starting node

    while queue:                 # Loop until the queue is empty
        node = queue.popleft()   # Remove and get the leftmost node
        if node not in visited:  # Check if node has not been visited
            print(node, end=" ") # Print the node
            visited.add(node)    # Mark node as visited
            # Add all unvisited neighbors to the queue
            for neighbor in tree[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

bfs(tree, 'A')  # Start BFS from node 'A'