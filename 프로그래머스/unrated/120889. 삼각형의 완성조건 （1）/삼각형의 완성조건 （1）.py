def solution(sides):
    answer = 0
    
    sides.sort()
    
    max_side = sides.pop()
    
    if sum(sides) > max_side:
        answer = 1
    else:
        answer = 2
    
    return answer