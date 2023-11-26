def solution(numbers):
    answer = 0
    temp = []
    
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            temp.append(numbers[i] * numbers[j])
            
    answer = max(temp)
    return answer