def solution(a, b):
    answer = 0
    
    temp = [int(str(a) + str(b)), 2*a*b]
    answer = max(temp)
    
    return answer