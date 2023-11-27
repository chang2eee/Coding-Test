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
    
    if temp:  # 마지막으로 처리되지 않은 temp가 있는지 확인
        answer += int(temp)

    return answer