def solution(my_string, alp):
    answer = ''
    
    for string in my_string:
        if alp not in my_string:
            answer = my_string
            break
        else:
            if string != alp:
                answer += string
            else:
                answer += string.upper()
    
    return answer