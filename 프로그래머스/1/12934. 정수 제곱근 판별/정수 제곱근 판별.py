from math import sqrt

def solution(n):
    answer = -1
        
    if sqrt(n) == n // sqrt(n):
        answer = pow(sqrt(n)+1, 2)
    
    return answer