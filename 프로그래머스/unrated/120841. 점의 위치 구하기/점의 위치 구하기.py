def solution(dot):
    answer = 0
    
    if 0 < dot[0] and 0 < dot[1]:
        answer = 1
    elif 0 > dot[0] and 0 < dot[1]:
        answer = 2
    elif 0 > dot[0] and 0 > dot[1]:
        answer = 3
    elif 0 < dot[0] and 0 > dot[1]:
        answer = 4
    else: pass
    
    return answer