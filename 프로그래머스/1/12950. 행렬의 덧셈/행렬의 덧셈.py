def solution(arr1, arr2):
    answer = []
    
    for element1, element2 in zip(arr1, arr2):
        temp = []
        
        for temp1, temp2 in zip(element1, element2):
            temp.append(temp1 + temp2)
        
        answer.append(temp)
        
    
    return answer