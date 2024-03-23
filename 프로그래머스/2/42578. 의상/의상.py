def solution(clothes):
    answer = 1
    closet = dict()
    
    for cloth in clothes:
        if cloth[1] not in closet:
            closet[cloth[1]] = [cloth[0]]
        else:
            closet[cloth[1]].append(cloth[0])
    
    for key, value in closet.items():
        answer *= len(value) +1
    
    
    return answer-1