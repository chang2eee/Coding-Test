def solution(my_string):
    answer = ''
    
    my_string = my_string.lower()
    my_string = list(my_string)
    my_string.sort()
    
    for element in my_string:
        answer += element
    
    return answer