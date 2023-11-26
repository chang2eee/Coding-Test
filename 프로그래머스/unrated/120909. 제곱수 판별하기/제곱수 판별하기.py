from math import sqrt

def solution(n):
    answer = 0
    
    temp = sqrt(n)
    
    if temp == int(temp):
        answer = 1  
    else:
        answer = 2  
    
    return answer
