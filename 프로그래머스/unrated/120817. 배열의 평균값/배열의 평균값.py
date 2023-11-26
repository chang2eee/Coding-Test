def solution(numbers):
    answer = 0
    
    for number in numbers:
        answer += number
        
    answer /= len(numbers)
    
    return answer