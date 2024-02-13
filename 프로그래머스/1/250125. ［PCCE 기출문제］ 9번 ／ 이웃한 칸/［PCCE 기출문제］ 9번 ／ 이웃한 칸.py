from collections import deque

def solution(board, h, w):
    answer = 0
    
    target = board[h][w]
    
    height, width = len(board), len(board[0])
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    queue = deque([(h, w)])
    
    while queue:
        y, x = queue.popleft()
        
        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]
            
            if 0 <= next_x < width and 0 <= next_y < height and board[next_y][next_x] == target:
                answer += 1
    
    
    return answer