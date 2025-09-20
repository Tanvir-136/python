from collections import deque

tree={
    'A':['B', 'E'],
    'B':['A','C','D'],
    'C':['B','F'],
    'D':['B'],
    'E':['A'],
    'F':['C']
}

def bidirectional(tree, start, goal):
    if start == goal:
        return None, None
    
    start_visited = []
    start_queue = deque([start])
    goal_visited = []
    goal_queue = deque([goal])
    
    while start_queue and goal_queue:
        start_node = start_queue.popleft()
        if start_node not in start_visited:
            start_visited.append(start_node)
            for neighbor in tree[start_node]:
                if neighbor not in start_visited:
                    start_queue.append(neighbor)
                    
        # from 
        goal_node = goal_queue.popleft()
        if goal_node not in goal_visited:
            goal_visited.append(goal_node)
            for neighbor in tree[goal_node]:
                goal_queue.append(neighbor)
                
        if start_node in goal_visited or goal_node in start_visited:
            return start_visited,goal_visited
        
print(bidirectional(tree,'A', 'D'))