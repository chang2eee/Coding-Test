def solution(arr, queries):
    answer = []
    
    for query in queries:
        s, e, k = query
        temp_list = arr[s:e+1]
        temp = []
        for element in temp_list:
            if element > k:
                temp.append(element)
                
        if temp:
            answer.append(min(temp))
        if not temp:
            answer.append(-1)
        
            
    
    return answer