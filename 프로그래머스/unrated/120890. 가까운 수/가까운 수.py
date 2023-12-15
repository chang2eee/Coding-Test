def solution(array, n):
    answer = 0
    dic = dict()
    
    for element in array:
        dic[element] = abs(n - element)
        
    dic = list(dic.items())
    dic = sorted(dic, key=lambda x: x[1])
    
    min_value = dic[0][1]
    temp = []
    
    for key, value in dic:
        if value == min_value:
            temp.append(key)
    
    answer = min(temp)
    
    return answer
