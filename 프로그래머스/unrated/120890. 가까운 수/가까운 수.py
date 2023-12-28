def solution(array, n):
    answer = 0
    
    dic = dict()
    
    for element in array:
        dic[element] = abs(element - n)
        
    dic = sorted(dic.items(), key=lambda x:x[1])
    
    temp = []
    
    min_value = dic[0][1]
    
    for key, value in dic:
        if value == min_value:
            temp.append(key)
    
    answer = min(temp)
    
    return answer