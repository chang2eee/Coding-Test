def solution(num_list):
    answer = 0
    sum_odd, sum_even = 0, 0
    
    for i in range(len(num_list)):
        if i % 2 == 0:
            sum_odd += num_list[i]
        else:
            sum_even += num_list[i]
    
    temp = [sum_odd, sum_even]
    
    answer = max(temp)
    
    return answer