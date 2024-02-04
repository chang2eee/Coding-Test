from math import ceil

def solution(progresses, speeds):
    answer = []
    
    progresses = [100 - progress for progress in progresses]
    days = []
    
    for progress, speed in zip(progresses, speeds):
        days.append(ceil(progress / speed))
    
    temp = []
    
    for day in days:
        if not temp:
            temp.append(day)
        else:
            if max(temp) >= day:
                temp.append(day)
            else:
                if max(temp) >= day:
                    temp.append(day)
                else:
                    answer.append(len(temp))
                    temp.clear()
                    temp.append(day)
            
    if temp:
        answer.append(len(temp))
                    
    return answer