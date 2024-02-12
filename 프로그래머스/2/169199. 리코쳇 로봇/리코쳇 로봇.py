from collections import deque

def solution(board):
    answer = 0

    start_x, start_y = 0, 0
    
    visited = set()
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'R':
                start_x, start_y = j, i
    
    queue = deque([(start_x, start_y, 0)])
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while queue:
        x, y, distance = queue.popleft()
        
        if (x, y) in visited:
            continue
            
        if board[y][x] == 'G':  
            return distance
        
        visited.add((x, y))
        
        for i in range(4):
            now_x = x
            now_y = y
            
            while True:
                next_x = now_x + dx[i]
                next_y = now_y + dy[i]
                
                if not (0 <= next_x < len(board[0]) and 0 <= next_y < len(board) and board[next_y][next_x] != 'D'):  
                    break
                
                now_x = next_x
                now_y = next_y
                
            queue.append((now_x, now_y, distance + 1))
    
    return -1
