def solution(order):
    answer = 0
    
    for element in str(order):
        if element == '3' or element == '6' or element == '9':
            answer += 1
    
    return answer