def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    temp = []
    
    for i in range(0, len(score), m):
        temp.append(score[i:i+m])
    
    for element in temp:
        if len(element) == m:
            answer += min(element) * m
    
    return answer