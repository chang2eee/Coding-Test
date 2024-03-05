from collections import deque

def bfs(start, end, maps):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    start_y, start_x = 0, 0
    end_y, end_x = 0, 0
    
    n, m = len(maps), len(maps[0])
    
    visited = [[False] * m for _ in range(n)]
    
    value = 0
    
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == start:
                start_y, start_x = i, j
            if maps[i][j] == end:
                end_y, end_x = i, j
                
    queue = deque([(start_y, start_x, value)])
    
    while queue:
        y, x, value = queue.popleft()
        
        if y == end_y and x == end_x:
            return value + 1
        
        for i in range(4):
            next_y = y + dy[i]
            next_x = x + dx[i]
            
            if 0 <= next_y <= len(maps) - 1 and 0 <= next_x <= len(maps[0]) - 1 and maps[next_y][next_x] != 0:
                if visited[next_y][next_x] == False:
                    queue.append((next_y, next_x, value + 1))
                    visited[next_y][next_x] = True
    
    return -1
    
    
    
    
    
    
    

def solution(maps):
    answer = 0
    maps[0][0] = 'S'
    maps[-1][-1] = 'E'
    
    answer = bfs('S', 'E', maps)
    
    return answer