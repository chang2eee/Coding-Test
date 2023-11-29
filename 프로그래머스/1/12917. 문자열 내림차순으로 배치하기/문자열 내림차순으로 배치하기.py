def solution(s):
    answer = ''
    temp_upper, temp_lower = [], []
    s = list(s)
    
    for alpha in s:
        if alpha.isupper():
            temp_upper.append(alpha)
        else:
            temp_lower.append(alpha)

    temp_upper.sort(reverse=True)
    temp_lower.sort(reverse=True)
    
    for element in temp_lower:
        answer += str(element)
    
    for element in temp_upper:
        answer += str(element)
            
            
    return answer