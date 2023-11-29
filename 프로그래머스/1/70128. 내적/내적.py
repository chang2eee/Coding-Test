def solution(a, b):
    answer = 0
    
    for element1, element2 in zip(a, b):
        answer += element1 * element2
    
    return answer