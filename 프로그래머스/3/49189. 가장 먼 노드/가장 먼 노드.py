from collections import deque

def solution(n, edge):
    answer = 0
    
    graph = dict()
    
    for node in edge:
        start, end = node
        
        if start not in graph:
            graph[start] = [end]
        else:
            graph[start].append(end)
        
        if end not in graph:
            graph[end] = [start]
        else:
            graph[end].append(start)
    
    
    visited = [-1] * (n+1)
    
    queue = deque([1])
    visited[1] = 0 
    
    while queue:
        x = queue.popleft()
        
        for next_node in graph[x]:
            if visited[next_node] == -1: 
                visited[next_node] = visited[x] + 1  
                queue.append(next_node)
    
    max_distance = max(visited)
    answer = visited.count(max_distance)
    
    return answer
