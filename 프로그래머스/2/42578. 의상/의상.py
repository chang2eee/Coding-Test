def solution(clothes):
    answer = 0
    dic = dict()
    
    for cloth in clothes:
        if cloth[1] not in dic:
            dic[cloth[1]] = [cloth[0]]
        else:
            dic[cloth[1]].append(cloth[0])
    
    temp = 1
    
    for key, value in dic.items():
        temp *= (len(dic[key]) + 1)
    
        
    answer = temp - 1
    
    return answer