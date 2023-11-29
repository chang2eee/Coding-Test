def is_valid(r, c, board):
    return (0 <= r < len(board)) and (0 <= c < len(board[0]))
    
def solution(board):
    danger = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]
    
    directions = [[0, 0], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]
    for r, row in enumerate(board):
        for c, char in enumerate(row):
            if char == 1:
                for dr, dc in directions:
                    if is_valid(r+dr, c+dc, board):
                        danger[r+dr][c+dc] = 1
    answer = 0
    for row in danger:
        for char in row:
            if char == 0:
                answer += 1
            
    return answer