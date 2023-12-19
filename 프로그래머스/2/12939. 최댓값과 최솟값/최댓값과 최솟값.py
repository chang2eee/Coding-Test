def solution(s):
    answer = ''
    s = s.split(' ')
    
    temp = []
    
    for element in s:
        temp.append(int(element))
    
    min_value = min(temp)
    max_value = max(temp)
    
    answer = str(min_value) + ' ' + str(max_value)
    
    return answer