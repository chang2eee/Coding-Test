def solution(num_list):
    answer = []
    
    for index in range(len(num_list)-1, -1, -1):
        answer.append(num_list[index])
    
    return answer