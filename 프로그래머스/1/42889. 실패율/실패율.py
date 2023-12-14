from collections import Counter

def solution(N, stages):
    answer = []
    
    counter = Counter(stages)
    counter = list(counter.items())
    print(counter)
    counter = sorted(counter)
    print(counter)
    
    dic = dict()
    temp = 0
    
    for key, value in counter:
        if key <= N:
            dic[key] = value / (len(stages) - temp)
            temp += value
        else:
            continue
    
    for i in range(1, N+1):
        if i not in dic:
            dic[i] = 0
    
    dic = sorted(dic.items(), key=lambda x:x[1], reverse=True)    
    print(dic)
    
    for x, y in dic:
        answer.append(x)
    
    
    return answer