from math import ceil

def solution(progresses, speeds):
    answer = []
    
    progresses = [100 - progress for progress in progresses]
    
    remain = []
    for progress, speed in zip(progresses, speeds):
        remain.append(ceil(progress / speed))
        
    temp = []
    
    for day in remain:
        if len(temp) == 0:
            temp.append(day)
        else:
            if max(temp) >= day:
                temp.append(day)
            else:
                answer.append(len(temp))
                temp.clear()
                temp.append(day)
    
    if len(temp) != 0:
        answer.append(len(temp))
            
    
    return answer