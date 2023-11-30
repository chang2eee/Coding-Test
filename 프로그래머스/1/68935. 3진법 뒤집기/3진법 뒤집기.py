def solution(n):
    answer = 0
    temp = []
    
    while n != 0:
        temp.append(n % 3)
        n //= 3
        
    for i in range(len(temp)):
        answer += temp[i] * pow(3, len(temp)-1 - i)
    
    
    
    
    return answer