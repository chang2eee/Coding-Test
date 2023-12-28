def solution(arr):
    answer = []
    length = len(arr)
    
    for i in range(getNumber(length) - length):
        arr.append(0)
    
    answer = arr.copy()

    return answer

def getNumber(number):
    result = 1
    
    while result < number:
        result *= 2
        
    return result