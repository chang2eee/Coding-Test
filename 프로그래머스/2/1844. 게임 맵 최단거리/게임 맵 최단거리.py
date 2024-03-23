from collections import deque

def bfs(maps, start, end, visited):
    dy, dx = [0, 0, -1, 1], [-1, 1, 0, 0]
    start_y, start_x, end_y, end_x = 0, 0, 0, 0
    
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == start:
                start_y, start_x = i, j
            if maps[i][j] == end:
                end_y, end_x = i, j
    distance = 0
    
    queue = deque([(start_y, start_x, distance)])
    visited[start_y][start_x] = True
    while queue:
        y, x, distance = queue.popleft()
        
        
        if y == end_y and x == end_x:
            return 1+distance
        
        for i in range(4):
            next_y = y + dy[i]
            next_x = x + dx[i]
            
            if 0 <= next_y <= len(maps)-1 and 0 <= next_x <= len(maps[0])-1 and maps[next_y][next_x] != 0:
                if visited[next_y][next_x] == False:
                    queue.append((next_y, next_x, distance+1))
                    visited[next_y][next_x] = True
    return -1

def solution(maps):
    answer = 0
    
    maps[0][0], maps[-1][-1] = 'S', 'E'
    visited = [[False] * len(maps[0]) for _ in range(len(maps))]
    return bfs(maps, 'S', 'E', visited)
    
    return answer