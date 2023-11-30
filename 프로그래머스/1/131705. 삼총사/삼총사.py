from itertools import combinations

def solution(number):
    answer = 0
    
    temp = list(combinations(number, 3))
    
    for element in temp:
        if sum(element) == 0:
            answer += 1
    
    return answer