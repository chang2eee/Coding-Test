from math import gcd

def solution(n, m):
    answer = []
    
    temp_gcd = gcd(n, m)
    
    answer.append(temp_gcd)
    
    temp_max = max(n, m)
    
    temp = temp_max // temp_gcd
    
    answer.append(temp * min(m, n))
    
    return answer