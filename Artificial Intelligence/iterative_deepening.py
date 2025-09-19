from collections import deque
tree = {
    'A':['B', 'C'],
    'B':['C','D'],
    'C':['F'],
    'D':[],
    'E':[]
}

def dls(tree, node, limit, visited):
    if limit < 0:
        return
    print(node, end=" ")
    visited.add(node)
    for neighbor in tree.get(node, []):
        if neighbor not in visited:
            dls(tree, neighbor, limit - 1, visited)

def it_dfs(tree, start, max_limit):
    for i in range(max_limit):
        print(f"Iteration {i + 1}: ", end = " ")
        dls(tree, start, i, set())
        print()
        
it_dfs(tree, 'A', 4)