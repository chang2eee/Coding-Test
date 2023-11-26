def solution(num_list):
    answer, index = -1, 0
    
    for number in num_list:
        if number < 0:
            return index
        else:
            index += 1
            answer = -1
    
    return answer