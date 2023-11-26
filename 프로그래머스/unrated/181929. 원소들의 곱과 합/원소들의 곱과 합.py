def solution(num_list):
    answer = 0
    
    temp = 1
    for number in num_list:
        temp *= number
    
    if pow(sum(num_list), 2) > temp:
        answer =  1
    
    return answer