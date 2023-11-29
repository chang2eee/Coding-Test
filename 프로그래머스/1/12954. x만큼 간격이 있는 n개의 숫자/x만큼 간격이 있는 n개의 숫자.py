def solution(x, n):
    answer = []
    temp = x
    
    while len(answer) != n:
        answer.append(x)
        x += temp
    
    return answer