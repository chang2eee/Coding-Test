from collections import deque

def solution(maps):
    answer = 0
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    N = len(maps)
    M = len(maps[0])
    
    queue = deque()
    queue.append((0, 0))

    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if (0 <= nx < N) and (0 <= ny < M) and (maps[nx][ny] == 1):
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx, ny))
        
    answer = maps[N-1][M-1]
    
    if maps[N-1][M-1] == 1:
        answer = -1
    
    
    
    return answer