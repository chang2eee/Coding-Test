from collections import deque

def bfs(maps, visited, y, x):
    days = 0
    
    visited[y][x] = True
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    queue = deque([(y, x)])
    
    while queue:
        y, x = queue.popleft()
        days += int(maps[y][x])
        
        for i in range(4):
            next_y = y + dy[i]
            next_x = x + dx[i]
            
            if 0 <= next_y <= len(maps) - 1 and 0 <= next_x <= len(maps[0]) - 1 and visited[next_y][next_x] == False:
                if maps[next_y][next_x] != 'X':
                    queue.append((next_y, next_x))
                    visited[next_y][next_x] = True
    
    return days

def solution(maps):
    answer = []
    
    n, m = len(maps), len(maps[0])
    
    visited = [[False] * m for _ in range(n)]
    
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] != 'X' and visited[i][j] == 0:
                answer.append(bfs(maps, visited, i, j))
    
    if answer:
        return sorted(answer)
    else:
        return [-1]
    
