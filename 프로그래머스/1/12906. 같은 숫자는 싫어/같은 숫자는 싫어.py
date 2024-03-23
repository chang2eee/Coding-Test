def solution(arr):
    answer = []
    temp = []
    
    for element in arr:
        if len(temp) == 0:
            answer.append(element)
            temp.append(element)
        else:
            if element in temp:
                continue
            else:
                answer.append(element)
                temp.clear()
                temp.append(element)
    
    return answer