def solution(array):
    answer = 0
    
    for element in array:
        answer += int(str(element).count('7'))
    
    return answer