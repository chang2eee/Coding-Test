def solution(num_list):
    answer = 0
    
    for number in num_list:
        while number != 1:
            if number % 2 == 0:
                number /= 2
                answer += 1
            else:
                number = (number - 1) / 2
                answer += 1
                
    
    return answer