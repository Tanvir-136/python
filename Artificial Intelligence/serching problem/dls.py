from collections import deque

tree = {
    'A':['B', 'C'],
    'B':['C','D'],
    'C':['F'],
    'D':[],
    'E':[]
}

def dfs_limited(tree, start, limit, visited=[]):
    if limit <= 0:
        return
    if start not in visited:
        print(start, end=" ")
        visited.append(start)
    for node in tree[start]:
        dfs_limited(tree, node, limit-1, visited)

dfs_limited(tree, 'A', 3)
