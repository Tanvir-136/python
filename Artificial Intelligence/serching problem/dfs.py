from collections import deque  

# Define the tree as a dictionary (adjacency list)
tree = {
    'A': ['B', 'E'],
    'B': ['C', 'D'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}
def dfs(tree, start, visited = []):
    if start not in visited:
        print(start, end= " ")
        visited.append(start)
    for node in tree[start]:
        dfs(tree, node , visited)

dfs(tree, 'A')  # Start BFS from node 'A'