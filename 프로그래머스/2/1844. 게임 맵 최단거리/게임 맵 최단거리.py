from collections import deque

def solution(maps):
    answer = 0
    
    N = len(maps)
    M = len(maps[0])
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    queue = deque()
    queue.append((0, 0))    # start
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):  # 4방향 다 가보기
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx <= N - 1 and 0 <= ny <= M - 1 and maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx, ny))
                
    answer = maps[N-1][M-1]
    
    if maps[N-1][M-1] == 1:
        answer = -1
    
    return answer