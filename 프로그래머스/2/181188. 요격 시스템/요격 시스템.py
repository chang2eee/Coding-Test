def solution(targets):
    answer = 0
    targets.sort(key=lambda x:[x[1], x[0]])
    start = 0
    
    for target in targets:
        if start <= target[0]:
            start = target[1]
            answer += 1
    
    return answer