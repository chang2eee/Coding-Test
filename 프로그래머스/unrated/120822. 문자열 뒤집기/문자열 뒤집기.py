def solution(my_string):
    answer = ''
    
    for index in range(len(my_string)-1, -1, -1):
        answer += my_string[index]
    
    return answer