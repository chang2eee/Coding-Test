def solution(my_string):
    answer = 0
    temp = ''
    
    for element in my_string:
        if element.isdigit():
            temp += str(element)
        else:
            if temp:
                answer += int(temp)
                temp = ''
    
    if temp: 
        answer += int(temp)

    return answer