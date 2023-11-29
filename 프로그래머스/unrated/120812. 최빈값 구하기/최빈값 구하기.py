from collections import Counter

def solution(array):
    answer = 0
    
    counter = Counter(array)
    counter = sorted(counter.items(), key=lambda x : x[1], reverse=True)
    print(counter)
    temp = 0
    
    for element in counter:
        
        if element[1] == counter[0][-1]:
            temp += 1
    
    if temp >= 2:
        answer = -1
    else:
        answer = counter[0][0]
    
    
    # if counter.count(counter[0][1]) >= 2:
    #     answer = -1
    # else:
    #     answer = counter[0][0]
    
    
    return answer