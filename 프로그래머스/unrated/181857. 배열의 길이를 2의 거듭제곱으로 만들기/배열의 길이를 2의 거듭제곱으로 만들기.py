def solution(arr):
    answer = arr.copy()
    
    for i in range(getNumber(len(arr)) - len(arr)):
        answer.append(0)
    
    return answer

def getNumber(number):
    i = 1
    result = 1
    
    while result < number:
        result *= 2
    
    return result