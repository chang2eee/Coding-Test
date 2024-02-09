from collections import Counter

def solution(weights):
    answer = 0
    
    dic = Counter(weights)
            
    for key in dic:
        if dic[key] > 1:
            answer += (dic[key] * (dic[key]-1)) / 2
        if key*2 in dic:
            answer += dic[key] * dic[2*key]
        if (key*2) / 3 in dic:
            answer += dic[key] * dic[key*2/3]
        if (key*3) / 4 in dic:
            answer += dic[key] * dic[key*3/4]

    
    return answer