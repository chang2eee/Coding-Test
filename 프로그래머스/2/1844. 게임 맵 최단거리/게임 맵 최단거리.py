from collections import deque

def solution(maps):
    answer = 0
    
    start_x, start_y = 0, 0
    
    width, height = len(maps), len(maps[0])
    
    queue = deque([(0, 0)])
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]
            
            if 0 <= next_x <= width-1 and 0 <= next_y <= height-1 and maps[next_x][next_y] == 1:
                maps[next_x][next_y] += maps[x][y]
                queue.append((next_x, next_y))
        
    answer = maps[width-1][height-1]
    
    if maps[width-1][height-1] == 1:
        answer = -1
    
    
    return answer