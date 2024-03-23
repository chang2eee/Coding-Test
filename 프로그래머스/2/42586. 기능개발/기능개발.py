from math import ceil

def solution(progresses, speeds):
    answer = []
    
    progresses = [100 - p for p in progresses]
    remain = []
    
    for p, s in zip(progresses, speeds):
        remain.append(ceil(p/s))
    
    temp = []
    
    for element in remain:
        if len(temp) == 0:
            temp.append(element)
        else:
            if element <= max(temp):
                temp.append(element)
            else:   # element < max(temp)
                answer.append(len(temp))
                temp.clear()
                temp.append(element)
                
    if temp:
        answer.append(len(temp))
    
    return answer