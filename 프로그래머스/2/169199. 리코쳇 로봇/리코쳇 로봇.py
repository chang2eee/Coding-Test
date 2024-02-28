from collections import deque

def solution(board):
    answer = 0
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    start_y, start_x = 0, 0
    
    # 방문 좌표 기록
    visited = set()
    
    # 로봇 위치 찾기
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'R':
                start_y, start_x = i, j
    
    # y, x, 거리
    queue = deque([(start_y, start_x, 0)])
    
    while queue:
        y, x, answer = queue.popleft()
        
        if (y, x) in visited:
            continue
        
        if board[y][x] == 'G':
            return answer
    
        visited.add((y, x))

        for i in range(4):
            now_y = y
            now_x = x
            
            while True:
                next_x = now_x + dx[i]
                next_y = now_y + dy[i]
                
                if not (0 <= next_y <= len(board) - 1 and 0 <= next_x <= len(board[0]) -1 and board[next_y][next_x] != 'D'):
                    break
                    
                now_x = next_x
                now_y = next_y
                
            queue.append((now_y, now_x, answer + 1))
    
    return -1