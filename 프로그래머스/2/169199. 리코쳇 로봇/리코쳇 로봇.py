from collections import deque

def bfs(board, start, end):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    start_y, start_x = 0, 0
    end_y, end_x = 0, 0
    
    # 시작 / 탈출 좌표 구하기
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == start:
                start_y, start_x = i, j
            if board[i][j] == end:
                end_y, end_x = i, j
    
    visited = set()
    value = 0
    
    queue = deque([(start_y, start_x, value)])
    
    while queue:
        y, x, value = queue.popleft()
        
        if y == end_y and x == end_x:
            return value
        
        # 방문한 좌표 체크
        if (y, x) in visited:
            continue
        visited.add((y, x))
        
        for i in range(4):
            now_y, now_x = y, x
            while True:
                next_y = now_y + dy[i]
                next_x = now_x + dx[i]
                
                if (0 <= next_y <= len(board)-1 and 0 <= next_x <= len(board[0])-1 and board[next_y][next_x] != 'D') == False:
                    break
                
                now_y = next_y
                now_x = next_x
                
            queue.append((now_y, now_x, value+1))
                
    return -1
            
def solution(board):
    answer = bfs(board, 'R', 'G')
    
    return answer
