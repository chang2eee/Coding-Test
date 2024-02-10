from math import comb

def solution(balls, share):
    answer = 0
    
    answer = comb(balls, share)
    
    return answer