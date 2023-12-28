def solution(my_string):
    answer = 0
    temp = ''
    
    for element in my_string:
        if element.isdigit():
            temp += element
        else:
            if len(temp) != 0:  
                answer += int(temp)
                temp = ''
    
    if len(temp) != 0:
        answer += int(temp)
                
    return answer