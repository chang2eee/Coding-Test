def solution(k, score):
    answer = []
    
    temp = []
    
    for s in score:
        if len(temp) < k:
            temp.append(s)
        else:
            if min(temp) < s:
                temp.remove(min(temp))
                temp.append(s)
                
        
        answer.append(min(temp))
    
    
    return answer