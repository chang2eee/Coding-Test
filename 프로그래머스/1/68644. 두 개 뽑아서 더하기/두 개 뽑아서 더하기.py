def solution(numbers):
    answer = []
    temp_set = set()
    
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            temp_set.add(numbers[i] + numbers[j])
    
    answer = list(temp_set)
    answer.sort()
    
    return answer