def solution(num_list, n):
    answer = []
    
    temp1, temp2 = num_list[:n], num_list[n:]
    
    answer = temp2 + temp1
    

    
    return answer