def solution(num_list):
    answer = 0
    temp_odd, temp_even = '', ''
    
    for number in num_list:
        if number % 2 == 1:
            temp_odd += str(number)
        else:
            temp_even += str(number)
            
    answer = int(temp_odd) + int(temp_even)
    
    return answer