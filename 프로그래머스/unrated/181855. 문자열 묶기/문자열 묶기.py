def solution(strArr):
    answer = 0
    temp_max = 0
    
    for element in strArr:
        temp_max = max(temp_max, len(element))
        
    dic = dict()
    
    for element in strArr:
        length = len(element)
        
        if length in dic:
            dic[length] += 1
        else:
            dic[length] = 1
        
    answer = max(dic.values())        
    
    
    return answer