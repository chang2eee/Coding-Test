def solution(a, b):
    answer = 0
    a, b = str(a), str(b)
    temp = []
    
    temp.append(a+b)
    temp.append(b+a)
    
    answer = int(max(temp))
    
    
    return answer