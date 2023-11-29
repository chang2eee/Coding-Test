from math import gcd

def solution(numer1, denom1, numer2, denom2):
    answer = []
    
    number = numer1 * denom2 + numer2 * denom1
    denom = denom1 * denom2
    
    temp = gcd(number, denom)
    
    answer = [number // temp, denom // temp]
    
    return answer