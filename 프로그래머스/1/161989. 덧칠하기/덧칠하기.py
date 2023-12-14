def solution(n, m, section):
    answer = 0
    start = 0
    
    for sect in section:
        if sect >= start:
            start = sect + m
            answer += 1
        else:
            continue
    
    return answer