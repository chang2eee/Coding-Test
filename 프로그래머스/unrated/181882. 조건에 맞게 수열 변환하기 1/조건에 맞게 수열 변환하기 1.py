def solution(arr):
    answer = []
    
    for element in arr:
        if element >= 50 and element % 2 == 0:
            answer.append(element / 2)
        elif element < 50 and element % 2 == 1:
            answer.append(element * 2)
        else:
            answer.append(element)
    
    return answer