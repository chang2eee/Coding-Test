def solution(my_string, num1, num2):
    answer = ''
    
    string_num1, string_num2 = my_string[num1], my_string[num2]
    
    for i in range(len(my_string)):
        if i == num1:
            answer += string_num2
        elif i == num2:
            answer += string_num1
        else:
            answer += my_string[i]
    
    return answer