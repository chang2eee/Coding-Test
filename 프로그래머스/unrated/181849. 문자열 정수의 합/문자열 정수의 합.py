def solution(num_str):
    answer = 0
    
    for number in num_str:
        answer += int(number)
    
    return answer