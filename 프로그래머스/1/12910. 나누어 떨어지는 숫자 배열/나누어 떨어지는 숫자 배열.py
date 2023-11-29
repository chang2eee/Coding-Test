def solution(arr, divisor):
    answer = []
    
    for element in arr:
        if element % divisor == 0:
            answer.append(element)
    
    if not answer:
        answer = [-1]
    
    answer.sort()
    
    return answer