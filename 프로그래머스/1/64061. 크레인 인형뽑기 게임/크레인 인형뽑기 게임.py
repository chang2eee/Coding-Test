def solution(board, moves):
    answer = 0
    
    for idx in range(len(moves)):
        moves[idx] -= 1
    
    stack = []
    
    for move in moves:
        col = 0
        
        while col < len(board[0]) and board[col][move] == 0:
            col += 1
        
        if col < len(board[0]):
            stack.append(board[col][move])
            board[col][move] = 0
        
            if len(stack) >= 2 and stack[-1] == stack[-2]:
                stack.pop()
                stack.pop()
                answer += 2

    
    return answer