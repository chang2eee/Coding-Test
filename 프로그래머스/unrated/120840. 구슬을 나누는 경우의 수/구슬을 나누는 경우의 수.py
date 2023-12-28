# from itertools import combinations

# def solution(balls, share):
#     answer = 0
#     pocket = []
    
#     for i in range(balls):
#         pocket.append(i)
    
#     answer = len(list(combinations(pocket, share)))
    
#     return answer

from math import comb

def solution(balls, share):
    answer = 0
    
    answer = comb(balls, share)
    
    return answer