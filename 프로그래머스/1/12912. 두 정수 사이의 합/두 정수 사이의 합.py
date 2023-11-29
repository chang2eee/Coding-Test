def solution(a, b):
    answer = 0
    
    start, end = min(a, b), max(a, b)
    
    for i in range(start, end+1):
        answer += i
    
    return answer