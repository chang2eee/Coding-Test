def solution(t, p):
    answer = 0
    
    temp = []
    
    for i in range(len(t) - len(p) + 1):
        temp.append(t[i:i+len(p)])
        
    for element in temp:
        if int(element) <= int(p):
            answer += 1
    
    return answer