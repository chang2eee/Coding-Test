def solution(board, h, w):
    answer = 0
    target = board[h][w]
    height, width = len(board), len(board[0])
    
    if check(h-1, w, height, width) and board[h-1][w] == target:
        answer += 1
    
    if check(h+1, w, height, width) and board[h+1][w] == target:
        answer += 1
    
    if check(h, w-1, height, width) and board[h][w-1] == target:
        answer += 1
    
    if check(h, w+1, height, width) and board[h][w+1] == target:
        answer += 1
    
    return answer

def check(col, row, height, width):
    return 0 <= col <= height - 1 and 0 <= row <= width - 1