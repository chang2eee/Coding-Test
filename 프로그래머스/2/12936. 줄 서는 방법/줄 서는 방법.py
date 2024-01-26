from math import factorial
from itertools import permutations

def solution(n, k):
    answer = []
    arr = [i for i in range(1, n+1)]
    
    while arr:
        temp = (k-1) // factorial(n-1)
        
        answer.append(arr.pop(temp))
        
        k = k % factorial(n-1)
        n -= 1
    
    
    
    return answer