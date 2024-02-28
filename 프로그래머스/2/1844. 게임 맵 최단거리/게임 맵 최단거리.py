from collections import deque

def solution(maps):
    answer = 0
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    queue = deque([(0, 0)])
    
    while queue:
        y, x = queue.popleft()
        
        for i in range(4):
            next_y = y + dy[i]
            next_x = x + dx[i]
            
            if 0 <= next_y <= len(maps) - 1 and 0 <= next_x <= len(maps[0]) - 1 and maps[next_y][next_x] == 1:
                maps[next_y][next_x] += maps[y][x]
                
                queue.append((next_y, next_x))
    
    answer = maps[-1][-1]
    
    if answer == 1:
        answer = -1
    
    return answer