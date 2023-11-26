def solution(my_string, letter):
    answer = ''
    
    for string in my_string:
        if string == letter:
            continue
        else:
            answer += string
    
    return answer