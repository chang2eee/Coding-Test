from collections import deque

def solution(board, h, w):
    answer = 0
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    start_y, start_x = h, w
    target = board[start_y][start_x]
    
    queue = deque([(start_y, start_x)])
    
    while queue:
        y, x = queue.popleft()
        
        for i in range(4):
            next_y = y + dy[i]
            next_x = x + dx[i]
            
            if 0 <= next_y <= len(board) - 1 and 0 <= next_x <= len(board[0]) - 1 and board[next_y][next_x] == target:
                answer += 1
    
    return answer