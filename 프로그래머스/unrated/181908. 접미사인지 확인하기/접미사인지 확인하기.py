def solution(my_string, is_suffix):
    answer = 0
    temp = []
    
    for i in range(len(my_string)):
        temp.append(my_string[i:])
    
    if is_suffix in temp:
        answer = 1
    
    return answer